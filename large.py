import pyfiglet 
from termcolor import colored 

text = "Hello Miss Coder"
fonts = ["slant"]  

for i, word in enumerate(text.split()):
    font = pyfiglet.Figlet(font=fonts[i % len(fonts)])
    color = ["blue","green","magenta","red"][i % 4]
    ascii_art = font.renderText(word)
    print(colored(ascii_art, color))