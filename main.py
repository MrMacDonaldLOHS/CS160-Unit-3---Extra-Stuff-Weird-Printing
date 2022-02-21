# Here is some stuff you never need to know for this class, but it demonstrates 
# The rarely used backspace escape character and the flush option that forces the
# string to come out immediately.
import time
print("I am typpping", end='', flush=True)
#Wait 1/2 a second between each call to print so that it looks more like typing
time.sleep(0.5)
#Go back one space, print a space to erase the letter, go back one space again
print("\b \b", end='', flush=True)
time.sleep(0.5)
print("\b \b", end='', flush=True)
time.sleep(0.5)
print("\b \b", end='', flush=True)
time.sleep(0.5)
print("\b \b", end='', flush=True)
time.sleep(0.5)
print("\b \b", end='', flush=True)
time.sleep(0.5)
print("ing   ")
