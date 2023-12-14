import csv
import os
import sys
import argparse

class MyArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        if 'the following arguments are required' in message:
            print('Error: You have to specify the symbol')
            self.print_help()
            sys.exit(1)
        super().error(message)

def getCSVPath():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'pse.csv')
    else:
        return 'pse.csv'

parser = MyArgumentParser(description='Periodic Cli by Molitvan - Periodic Table in your terminal', epilog=f'Example: {sys.argv[0]} Ag (get information about gold)')

parser.add_argument('symbol', help='The symbol of an element')
parser.add_argument('-z', '--atomic-number', help='Show the atomic number', action='store_true')
parser.add_argument('-a', '--atomic-mass', help='Show the atomic mass', action='store_true')
parser.add_argument('-m', '--average-atomic-mass', help='Show the average atomic mass', action='store_true')
parser.add_argument('-g', '--group', help='Show the group number in the periodic table', action='store_true')
parser.add_argument('-p', '--period', help='Show the period number in the periodic table', action='store_true')

args = parser.parse_args()

element = args.symbol.capitalize()

with open(getCSVPath(), 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    symbolIndex = header.index('symbol')
    atomicNumberIndex = header.index('number')
    atomicMassIndex = header.index('atomic_mass')
    periodIndex = header.index('ypos')
    groupIndex = header.index('xpos')

    for row in reader:
        if row[symbolIndex] == element:

            if not args.atomic_number and not args.atomic_mass and not args.average_atomic_mass and not args.group and not args.period:
                print(f'Element: {element}')
                print(f'Period: {row[periodIndex]}')
                print(f'Group: {row[groupIndex]}')
                print(f'Atomic number: {row[atomicNumberIndex]}')
                print(f'Atomic mass: {round(float(row[atomicMassIndex]))}')

                sys.exit(0)

            if args.period: print(row[periodIndex])
            if args.group: print(row[groupIndex])
            if args.atomic_number: print(row[atomicNumberIndex])
            if args.atomic_mass: print(round(float(row[atomicMassIndex])))
            if args.average_atomic_mass: print(row[atomicMassIndex])
            
            sys.exit(0)

print('There is no element with that symbol.')
