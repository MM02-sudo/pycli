#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Py cli tool")

parser.add_argument('command',
                    choices=['add', 'list 'search', 'delete'],
                    help='Usable commands')

args = parser.parse_args()

print(f"You entered command: {args.command}")


