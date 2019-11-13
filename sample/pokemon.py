import subprocess, argparse, time

parser = argparse.ArgumentParser()

#Adding arguments
parser.add_argument("game", help="specify which game to load", choices=["blue", "red"])

args = parser.parse_args()

if args.game.lower() == "blue":
    print("Loading 'Pokemon Mystery Dungeon: Blue Rescue Team'")
elif args.game.lower() == "red":
    print("Loading 'Pokemon Mystery Dungeon: Red Rescue Team'")

