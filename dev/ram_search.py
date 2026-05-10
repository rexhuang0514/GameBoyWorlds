"""
RAM search tool for finding GBC memory addresses.

Commands:
  snapshot    - take a WRAM baseline snapshot
  c/changed   - keep only addresses that changed since last snapshot
  unchanged   - keep only addresses that did NOT change
  eq N        - keep only addresses whose current value == N
  gt N        - keep only addresses whose current value > N
  lt N        - keep only addresses whose current value < N
  print       - show current candidates, up to 40
  watch 0xADDR [0xADDR2 ...] - live-print values every 0.5 s; Enter to stop
  reset       - restore all 8192 WRAM candidates
  q           - quit
"""

import os
import queue
import sys
import threading

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")
for path in (SRC_ROOT, PROJECT_ROOT):
    if path not in sys.path:
        sys.path.insert(0, path)

import click
import numpy as np

from gameboy_worlds import AVAILABLE_GAMES, get_emulator

WRAM_START = 0xC000
WRAM_END = 0xDFFF


def read_wram(pyboy) -> np.ndarray:
    size = WRAM_END - WRAM_START + 1
    arr = np.empty(size, dtype=np.uint8)
    for i in range(size):
        arr[i] = pyboy.memory[WRAM_START + i]
    return arr


@click.command()
@click.option("--game", type=click.Choice(AVAILABLE_GAMES), default="survival_kids_2")
@click.option("--init_state", default=None)
def main(game, init_state):
    emulator = get_emulator(
        game=game,
        init_state=init_state,
        headless=False,
        save_video=False,
    )
    pyboy = emulator._pyboy

    candidates = list(range(WRAM_END - WRAM_START + 1))
    last_snap = None
    watch_addrs = []
    alive = True
    cmd_q = queue.Queue()

    def _input_loop():
        while True:
            try:
                line = input("ram> ")
            except (EOFError, KeyboardInterrupt):
                cmd_q.put("q")
                return
            cmd_q.put(line.strip())
            if line.strip().lower() in ("q", "quit", "exit"):
                return

    threading.Thread(target=_input_loop, daemon=True).start()

    print(
        f"RAM search - {len(candidates)} candidates. "
        f"Game running in window. Type 'help'.\n"
    )

    frame = 0
    try:
        while alive:
            # SDL2 window events must be pumped from the main thread.
            pyboy.tick(1, True)
            frame += 1

            if watch_addrs and frame % 30 == 0:
                vals = "  ".join(
                    f"0x{addr:04X}={pyboy.memory[addr]:3d}" for addr in watch_addrs
                )
                sys.stdout.write(f"\r{vals}    ")
                sys.stdout.flush()

            try:
                raw = cmd_q.get_nowait()
            except queue.Empty:
                continue

            parts = raw.strip().lower().split()

            if not parts:
                if watch_addrs:
                    watch_addrs.clear()
                    print("\nWatch stopped.")
                continue

            op = parts[0]

            if op in ("q", "quit", "exit"):
                alive = False

            elif op == "help":
                print(__doc__)

            elif op == "snapshot":
                last_snap = read_wram(pyboy)
                print(f"Snapshot taken. {len(candidates)} candidates.")

            elif op in ("c", "changed"):
                if last_snap is None:
                    print("No snapshot yet - run 'snapshot' first.")
                else:
                    cur = read_wram(pyboy)
                    candidates = [i for i in candidates if cur[i] != last_snap[i]]
                    last_snap = cur
                    print(f"{len(candidates)} candidates changed.")

            elif op == "unchanged":
                if last_snap is None:
                    print("No snapshot yet - run 'snapshot' first.")
                else:
                    cur = read_wram(pyboy)
                    candidates = [i for i in candidates if cur[i] == last_snap[i]]
                    last_snap = cur
                    print(f"{len(candidates)} candidates unchanged.")

            elif op in ("eq", "gt", "lt"):
                if len(parts) < 2:
                    print(f"Usage: {op} <value>")
                    continue
                try:
                    val = int(parts[1], 0)
                except ValueError:
                    print(f"Value must be an integer, e.g. '{op} 12' or '{op} 0x0c'.")
                    continue
                cur = read_wram(pyboy)
                fns = {
                    "eq": lambda x: x == val,
                    "gt": lambda x: x > val,
                    "lt": lambda x: x < val,
                }
                candidates = [i for i in candidates if fns[op](cur[i])]
                print(f"{len(candidates)} candidates {op} {val}.")

            elif op == "print":
                cur = read_wram(pyboy)
                show = candidates[:40]
                print()
                for off in show:
                    print(f"  0x{WRAM_START + off:04X}  =  {cur[off]}")
                if len(candidates) > 40:
                    print(f"  ... and {len(candidates) - 40} more.")
                if not candidates:
                    print("  (empty - type 'reset' to start over)")

            elif op == "watch":
                if len(parts) < 2:
                    print("Usage: watch <hex_addr> [hex_addr2 ...]")
                    continue
                try:
                    addrs = [int(addr, 16) for addr in parts[1:]]
                except ValueError:
                    print("Addresses must be hex, e.g.: watch 0xC0A0")
                    continue
                invalid = [addr for addr in addrs if addr < WRAM_START or addr > WRAM_END]
                if invalid:
                    print(
                        "Addresses must be in WRAM range "
                        f"0x{WRAM_START:04X}-0x{WRAM_END:04X}: "
                        + ", ".join(f"0x{addr:04X}" for addr in invalid)
                    )
                    continue
                watch_addrs[:] = addrs
                print("Watching - press Enter to stop...")

            elif op == "reset":
                candidates = list(range(WRAM_END - WRAM_START + 1))
                print(f"Reset to {len(candidates)} candidates.")

            else:
                print(f"Unknown command '{op}'. Type 'help'.")
    finally:
        emulator.close()
    print("Done.")


if __name__ == "__main__":
    main()
