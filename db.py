#!/usr/bin/python
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Process some module or DB migration.')
parser.add_argument('string', metavar='N', type=str,
                   help='The name of the module to migrate using the local settings')

args = parser.parse_args()
print("Will run the following commands::")
print("\tpython manage.py schemamigration "+args.string+" --auto")
print("\tpython manage.py migrate "+args.string+"")
print("-----")
print("Schema Migration::")
subprocess.Popen(['python','manage.py','schemamigration',args.string,'--auto']).wait()
print("Migrate::")
subprocess.Popen(['python','manage.py','migrate',args.string]).wait()