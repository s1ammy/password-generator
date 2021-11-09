## This is a web program that generate password of arbitrary length

---

Code:

```Python
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
```
## Explanation

---

There are importnant imports:
```Python
from pywebio.input import *
from pywebio.output import *
import random
```
There are all possible symbols of password:
```Python
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "[]{}(),.!?_*/-"
all_signs = lower + upper + numbers + symbol
```

There are input of password length and password generating function:
```Python
length = input("Enter the length of password: ", type=NUMBER, placeholder="Length")
password = "".join(random.sample(all_signs, length))
```

Here is random generated password output:
```Python
put_text("The generated password is: ").style("font-size: 50px")
put_text(password).style("font-size: 50px; color: blue")
```
