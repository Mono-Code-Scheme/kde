#!/bin/python

import subprocess
import os
from pathlib import Path

RED_TEXT = "\033[31m"
GREEN = "\033[32m"
COLOR_END = "\033[0m"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_COLOR_SCHEMES_DIR = os.path.expanduser("~") + "/.local/share/color-schemes"

color_scheme_path = SCRIPT_DIR + "/schemes"

print("Select the base theme:")
print("1) Panther")
print("2) Lynx")

base_option = input("> ")

if base_option not in ["1", "2"]:
    print(RED_TEXT + "Invalid Option" + COLOR_END)

print("\nSelect the accent color:")
print("1) Red")
print("2) Orange")
print("3) Yellow")
print("4) Green")
print("5) NeonGreen")
print("6) Cyan")
print("7) Blue")
print("8) Purple")
print("9) Pink")

accent_option = input("> ")

if accent_option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    print(RED_TEXT + "Invalid Option" + COLOR_END)


if base_option == "1":
    color_scheme_path += "/panther/MonoCodePanther"
else:
    color_scheme_path += "/lynx/MonoCodeLynx"


if accent_option == "1":
    color_scheme_path += "Red"
elif accent_option == "2":
    color_scheme_path += "Orange"
elif accent_option == "3":
    color_scheme_path += "Yellow"
elif accent_option == "4":
    color_scheme_path += "Green"
elif accent_option == "5":
    color_scheme_path += "NeonGreen"
elif accent_option == "6":
    color_scheme_path += "Cyan"
elif accent_option == "7":
    color_scheme_path += "Blue"
elif accent_option == "8":
    color_scheme_path += "Purple"
else:
    color_scheme_path += "Pink"

color_scheme_path += ".colors"

subprocess.run(f"mkdir -p '{LOCAL_COLOR_SCHEMES_DIR}'", shell=True)
subprocess.run(f"cp '{color_scheme_path}' '{LOCAL_COLOR_SCHEMES_DIR}'", shell=True)

theme_name = Path(color_scheme_path).stem

apply_theme = input("Would you like to apply the theme? [Y/n]: ")

if apply_theme.lower() in ["n", "no"]:
    exit(0)

subprocess.run(f"plasma-apply-colorscheme {theme_name}", shell=True)
