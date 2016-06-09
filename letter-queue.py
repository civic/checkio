def letter_queue(commands):
    queue = ""
    for cmd in commands:
        if cmd.startswith("PUSH "):
            queue += cmd[-1]
        elif cmd == "POP" and len(queue) > 0:
            queue = queue[1:]

    return queue

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
