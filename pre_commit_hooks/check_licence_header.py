from __future__ import annotations

import argparse
from typing import Any, Sequence


LICENCE_HEADER_TEXT = """// Copyright © 2022 Obol Technologies Inc.
//
// This program is free software: you can redistribute it and/or modify it
// under the terms of the GNU General Public License as published by the Free
// Software Foundation, either version 3 of the License, or (at your option)
// any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or
// FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
// more details.
//
// You should have received a copy of the GNU General Public License along with
// this program.  If not, see <http://www.gnu.org/licenses/>."""

def prepend_licence_header(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(LICENCE_HEADER_TEXT.rstrip('\r\n') + '\n\n' + content)

def isLicenceHeaderPresent(filename: Any) -> bool:
    with open(filename, 'r') as f:
        content = f.read()
        return content.startswith(LICENCE_HEADER_TEXT)

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        if not isLicenceHeaderPresent(filename):
            prepend_licence_header(filename)
            print(f'Fixing {filename}')
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
