# wayne w 2020
# needs siggen/tones and aoss
# aoss is a compat program to  use tones that relies on /dev/dsp which has been dropped
#aoss tones -w seq.wav 70 1016 1200 1080 1150 1016
#aoss tones 50 1000 700,1200 800,1100,1300
#     tones len of 50 millisecs ^

#import time
from os import system

print("Enter a message to be translated into tones. The message will be recorded in the current directory in .wav format.")
msg = "test"
msg = str(input("Enter message: "))
msg = msg.upper()
tone_length = 100
tones = {"A":500,"B":550,"C":600,"D":650, "E":700, "F":750,"G":800, "H":850, "I":900, "J":950, "K":1000, "L":1050,
"M":1100, "N":1150, "O":1200, "P":1250, "Q":1300, "R":1350,"S":1400, "T":1450, "U":1500, "V":1550, "W":1600, "X":1650,"Y":1700,"Z":1750, "BLANK":1}

# for tones prog
def store_tone(message):
	tone_command_string=""
	for letter in message:
		if letter.isalpha():
			tone_command_string+=str(tones[letter]) + " "
		else:
			tone_command_string+=str(tones["BLANK"]) + " "
	return tone_command_string


                    #time.sleep(.2)
result_string = store_tone(msg)
print (result_string)
system("/usr/bin/aoss tones -w message.wav " + str(tone_length) +" "+result_string)

