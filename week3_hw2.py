import argparse
import pathlib
from pathlib import Path
import datetime


parser = argparse.ArgumentParser(
    prog="lists",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
    )
general = parser.add_argument_group("general output")
general.add_argument(
    "path",
    nargs="?",
    default=".",
    help="take the path to target directory (default: %(default)s)",
)
detailed = parser.add_argument_group("detailed output")
detailed.add_argument(
    "-l",
    "--long",
    action="store_true",
    default=".",
    help="display detailed diretory content",
)
parser.add_argument("path")
# parser.add_argument("-l", "--long", action="store_true")
args = parser.parse_args()
target_dir = Path(args.path)

if not target_dir.exists():
    print(f'The target directory doesn\'t exist')
    raise SystemExit(1)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
                "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    
    return entry.name

for item in target_dir.iterdir():
    print(build_output(item, long=args.long))