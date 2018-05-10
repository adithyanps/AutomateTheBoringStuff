import webbrowser, sys
import pyperclip
if len(sys.argv) > 1:
 address=' '.join(sys.argv[1:])
else:
 adress=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/Govt.+Engineering+College+Palakkad/@10.8945323,76.4447365,13.25z/data=!4m5!3m4!1s0x0:0xecf06761ecf4f56c!8m2!3d10.9035521!4d76.4347386')
