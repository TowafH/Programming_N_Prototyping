# Towaf Hossain
# 11/19/24
# PD 1-2
# description: Create a Ringtone using a Piano
from earsketch import *

init()
setTempo(120)

# Sound Variables
pianoBright = IRCA_BOMBA_SEIS_CORRIDO_ELEC_PIANO
ciaraBeat = CIARA_MELANIN_DRUMBEAT_1
drums8Bit = EIGHT_BIT_ANALOG_DRUM_LOOP_020
pianoFaster = IRCA_BOMBA_HOLANDE_PIANO
pianoMedium = IRCA_BOMBA_SICA_CORTIJO_PIANO

# Beat Variables
clapBeat = "0-0--000"

# A-B-A Functions
def sectionA():
    fitMedia(pianoBright, 2, 1, 13)  # Play pianoBright in Section A
    #setEffect(track, type, parameter, startValue, start, endValue, end)
    setEffect(2, VOLUME, GAIN, -15, 9, 1, 13)  # Add volume effect to track 2

def sectionB():
    fitMedia(pianoFaster, 3, 13, 21)  # Play pianoFaster in Section B

def sectionAReturn():
    fitMedia(pianoMedium, 2, 21, 33)  # Play pianoMedium for return of Section A

def addPercussion():
    fitMedia(ciaraBeat, 4, 5, 33)  # Play ciaraBeat throughout
    for measure in range(1, 34):  # Add drum beats up to measure 33
        makeBeat(drums8Bit, 5, measure, clapBeat)

#Ending Function
def ending():
    fitMedia(pianoMedium, 2, 33, 36)
    #setEffect(track, type, parameter, startValue, start, endValue, end)
    setEffect(2, VOLUME, GAIN, 5, 29, -20, 36)  # Fade out volume
    fitMedia(drums8Bit, 5, 30, 36) 
    setEffect(5, VOLUME, GAIN, -10, 34, -30, 36)  # Fade out the drum volume

# Calling Functions
sectionA()         # Play Section A
sectionB()         # Play Section B
sectionAReturn()   # Play Section A Again
addPercussion()    # Add percussion to the track
ending()           # Add an ending section

finish()
