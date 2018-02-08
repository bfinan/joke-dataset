import sys
from subprocess import call
import random
import pandas as pd
sys.path.insert(0, '/home/you/ml/joke-dataset/scripts')
from jokeutils import parse_args
from colors import bcolors

def reprint(index):
    call(["clear"])
    print(bcolors.OKGREEN + str(index))
    print()
    print(" " + bcolors.FAIL + df["Question"][index])
    print()
    print(" " + bcolors.OKBLUE  + df["Answer"][index] + bcolors.ENDC)
    print()

infile = parse_args()
df = pd.read_csv(infile)
homerow5 = "asdfg"
homerow3 = "jkl"
ratestring = bcolors.WARNING + "Rate the Joke:\n"
for i in range(0,5):
    ratestring += "[" + bcolors.BOLD + homerow5[i].upper() + bcolors.ENDC + bcolors.WARNING +"]"
    ratestring += "  " + ("★ " * (i+1)) + "\n"
    


dirtstring = bcolors.EXPERIMENTAL + "Dirtiness:\n"

dirtratings = ["clean", "mild", "dirty"]

for i in range(0,3):
    dirtstring += "[" + bcolors.BOLD + homerow3[i].upper() + bcolors.ENDC + bcolors.EXPERIMENTAL + "]"
    dirtstring += "  " + dirtratings[i] + "\n"

index = int(input('Choose a starting index: '))
stop = False
write = True

while stop is False and index < len(df):

    reprint(index)
    print("Commands:")
    print("[P]un\n[D]elete\n[E]xit\n[B]ack\n[G]oto\n[2] - Duplicate joke\n")
    commandKey = input().lower()
    if 'p' in commandKey:
        df.loc[df.index[index], "meta"] += ("genre:pun ")
    if 'd' in commandKey:
        df.loc[df.index[index], "meta"] += ("mark:delete ")
    if 'e' in commandKey:
        stop = True
        break
    if 'g' in commandKey:
        print("This is where I would put the function... if I had implemented it...")
    if 'b' in commandKey:
        index -= 1
    if '2' in commandKey:
        df.loc[df.index[index], "meta"] += ("mark:duplicate ")
        
    reprint(index)
    while df.loc[df.index[index], "rating"] == 0:

        ratekey = input(ratestring).lower()
        if ratekey in homerow5:
            rating = homerow5.find(ratekey) + 1
            print(('★ ' * rating))
            df.loc[df.index[index], "rating"] = rating
        else:
            print("Invalid key")
            
    reprint(index)
    while "dirt" not in df.loc[df.index[index], "meta"]:
        ratekey = input(dirtstring).lower()
        if ratekey in homerow3:
            df.loc[df.index[index], "meta"] += ("dirt:" + dirtratings[homerow5.find(ratekey)])
        else:
            print("Invalid key")
    index += 1

if write is True:
    print("Writing...")
    df.to_csv(scorefile, encoding='utf-8', index=False)




