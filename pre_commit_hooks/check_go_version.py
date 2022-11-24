from __future__ import annotations

import argparse
import os
from typing import Sequence
from packaging.version import Version   # works for go module versions since go follows semantic versioning

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    print("argv", argv)

    parser.add_argument(
        '-v',
        '--version',
        default='1.19',
        action="store",
        required=True,
        help="expected go version. Ex: 1.19 or 1.19.3",
    )
    args = parser.parse_args(argv)

    # get expected minimum go version
    reqVersion = args.version
    if reqVersion is None or not reqVersion.startswith("go"):
        return 1

    # get system go version
    stream = os.popen('go env GOVERSION')
    gotVersion = stream.read()

    # `go env GOVERSION` outputs go version with the `go` prefix. For ex: go1.19.2
    if Version(gotVersion[2:]) < Version(reqVersion[2:]):
        print("need to upgrade go version to", reqVersion, "or more")
        return 1

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
