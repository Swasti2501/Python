from colorama import Fore

def heart_shape(msg="Welcome to my code"):
    lines = []
    msg_length = len(msg)
    msg_index = 0  
    for y in range(15, -15, -1):
        line = ""
        for x in range(-30, 30):
            f = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if f <= 0:

                line += msg[msg_index % msg_length]

                msg_index += 1
            else:
                line += " "
        lines.append(line)

    print(Fore.WHITE + "\n".join(lines))

heart_shape()
