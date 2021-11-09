from pywebio.input import *
from pywebio.output import *
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "[]{}(),.!?_*/-"
all_signs = lower + upper + numbers + symbol

length = input("Enter the length of password: ", type=NUMBER, placeholder="Length")
password = "".join(random.sample(all_signs, length))

put_text("The generated password is: ").style("font-size: 50px")
put_text(password).style("font-size: 50px; color: blue")
