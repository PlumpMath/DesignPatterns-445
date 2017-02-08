import argparse
import os

parser = argparse.ArgumentParser(description='Scaffolding tool for simple Python projects', epilog='Report any issues to [Github url]')
parser.add_argument('-p','--project',required=True, nargs=1, help='The name of the project to create')
parser.add_argument('-d','--dir',required=False, nargs=1, help='The directory in which to create the project (creates in current directory by default)')

args = parser.parse_args()
cur_dir = os.getcwd()

if args.dir != None:
    cur_dir = args.dir[0]

def main():
    try:
        create_project(args.project[0], cur_dir)
    except IOError as e:
        print(e.strerror)

if __name__ == "__main__":
    main()
