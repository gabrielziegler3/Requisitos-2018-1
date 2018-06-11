import os
import subprocess

path = input("Insert path containing lexers: ")
os.chdir(path)

lexers = {
    'Streamer': '[Streamer](Streamer)',
    'streamer': '[streamer](Streamer)',
    'Streamers': '[Streamers](Streamer)',
    'streamers': '[streamers](Streamer)',
    'Viewer': '[Viewer](Viewer)',
    'viewer': '[viewer](Viewer)',
    'Clipe': '[Clipe](Clipe)',
    'clipe': '[clipe](Clipe)',
    'Whisper': '[Whisper](Whisper)',
    'whisper': '[whisper](Whisper)',
    'Streamar': '[Streamar](Streamar)',
    'streamar': '[streamar](Streamar)',
    'Streaming': '[Streaming](Streaming)',
    'streaming': '[streaming](Streaming)',
    'Raid': '[Raid](Raid)',
    'raid': '[raid](Raid)',
    'Ban': '[Ban](Ban)',
    'ban': '[ban](Ban)',
    'Donate': '[Donate](Donate)',
    'donate': '[donate](Donate)',
    'Share': '[Share](Share)',
    'share': '[share](Share)',
    'Mods': '[Mods](Mods)',
    'mods': '[mods](Mods)',
    'Chat': '[Chat](Group-Chat)',
    'chat': '[chat](Group-Chat)',
    'Follower': '[Follower](Follower)',
    'follower': '[follower](Follower)',
    'followers': '[followers](Follower)',
    }

regexes = {}

for k, v in lexers.items():
    match = ' ' + k + "$"
    replacement = ' ' + v
    regexes[match] = replacement

print(f"Working on {os.getcwd()}\n")
print(f"Looking for regexes: {regexes.keys()}\n")

for match, replacement in regexes.items():
    sed_arg = '"s/' + match + '/' + replacement + '/g"'
    command = f'sed -i {sed_arg} *.md'
    subprocess.call([command], shell=True)

print('Done linking all given lexers!!!')
