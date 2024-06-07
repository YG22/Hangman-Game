
from sty import fg
from sty import Style, RgbFg
# print('\033[95m', "x") # violate
# print('\033[94m', "x") # blue
# print('\033[96m', "x") # blue light
# print('\033[92m', "x") # green
# print('\033[93m', "x") # yellow
# print('\033[91m', "red") # red
# print('\033[0m', "x") # regular
# print('\033[1m', "x") # bold
# print('\033[4m', "x") # undrline
# print('\x1b[97m' , "x") # white
# print('\x1b[30m' , "x") # black
# print('\x1b[90m' , "x") # DarkGray
# print('\33[37m' , "x")
from sty import fg
red = fg(255, 10, 10) + 'red' 
orange = fg(255, 128, 0) + 'orange'
lightOrange = fg(255, 178, 102)+ 'lightOrange'
lightYellow = fg(255, 255, 153)+ 'lightYellow'
# Add custom colors:
print(lightYellow)
print('\033[93m' ,"yellow")
print(lightOrange)
print(orange)
print('\033[91m', "lIGHTred") # red
print(red)



## Formatting

# Bold = "\x1b[1m"
# Dim = "\x1b[2m"
# Italic = "\x1b[3m"
# Underlined = "\x1b[4m"
# Blink = "\x1b[5m"
# Reverse = "\x1b[7m"
# Hidden = "\x1b[8m"

## Background

# B_Default = "\x1b[49m"
# B_Black = "\x1b[40m"
# B_Red = "\x1b[41m"
# B_Green = "\x1b[42m"
# B_Yellow = "\x1b[43m"
# B_Blue = "\x1b[44m"
# B_Magenta = "\x1b[45m"
# B_Cyan = "\x1b[46m"
# B_LightGray = "\x1b[47m"
# B_DarkGray = "\x1b[100m"
# B_LightRed = "\x1b[101m"
# B_LightGreen = "\x1b[102m"
# B_LightYellow = "\x1b[103m"
# B_LightBlue = "\x1b[104m"
# B_LightMagenta = "\x1b[105m"
# B_LightCyan = "\x1b[106m"
# B_White = "\x1b[107m"

