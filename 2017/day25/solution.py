from collections import defaultdict

def main():
    tape: dict[int, int] = defaultdict(lambda: 0)
    cursor: int = 0
    state: str = "A"

    for i in range(12386363):
        val = tape[cursor]
        if state == "A":
            if val == 0:
                tape[cursor] = 1
                cursor += 1
                state = "B"
            else:
                tape[cursor] = 0
                cursor -= 1
                state = "E"
        elif state == "B":
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "C"
            else:
                tape[cursor] = 0
                cursor += 1
                state = "A"
        elif state == "C":
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "D"
            else:
                tape[cursor] = 0
                cursor += 1
                state = "C"
        elif state == "D":
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "E"
            else:
                tape[cursor] = 0
                cursor -= 1
                state = "F"
        elif state == "E":
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "A"
            else:
                tape[cursor] = 1
                cursor -= 1
                state = "C"
        elif state == "F":
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "E"
            else:
                tape[cursor] = 1
                cursor += 1
                state = "A"
        else:
            print("Broken state!")
            return
    print(f"Working! {sum(tape.values())}")

if __name__ == "__main__":
    main()
