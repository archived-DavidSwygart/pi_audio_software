#!/usr/bin/python3
import os
import warnings
import argparse, datetime, time

#Parse recording settings
parser = argparse.ArgumentParser(description='Record audio.')
parser.add_argument('--autoSaveInterval', '-a', 
                    help='Length of each audiofile in minutes (default 5)',
                    default='5')
parser.add_argument('--sampleRate', '-r', 
                    help='Sample rate (default 250,000 Hz)',
                    default='250000')
parser.add_argument('--session', '-s', 
                    help='Name session, which determines the folder name in which the video will be saved. Defaults to date and time'
                    )
parser.add_argument('--heterodyne', '-z', 
                    help='Heterodyne frequency for audio output (default 20,000 Hz)',
                    default='20000')

args = parser.parse_args()

if args.session is None:
    session = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
else:
    session = args.session

scriptPath = os.path.dirname(__file__)
hostname = os.uname().nodename
saveDirectory = scriptPath + '/audio/' + session + '/' + hostname
if os.path.exists(saveDirectory):
    warnings.warn("directory already exists for "+session+". Other videos could already be in "+saveDirectory)
else:
    os.makedirs(saveDirectory)
print('SavingFile in '+saveDirectory)

c= 'AudioMoth-Live ' + args.sampleRate
c=c + ' autosave ' + args.autoSaveInterval + ' ' + saveDirectory
c=c + ' heterodyne ' + args.heterodyne

print('starting audio recording')
os.system(c)
print('recordAudio.sh finished')
