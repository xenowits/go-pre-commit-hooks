from __future__ import annotations

import argparse
from typing import Any, Sequence


LICENCE_HEADER_TEXT = """// Copyright © 2021 Obol Technologies Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License."""

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

    print(args.filenames)
    return_code = 0
    for filename in args.filenames:
        print(f'Filename {filename}', isLicenceHeaderPresent(filename))
        if not isLicenceHeaderPresent(filename):
            prepend_licence_header(filename)
            print(f'Fixing {filename}')
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
