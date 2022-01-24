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
        type=str,
        action="store",
        required=True,
        help="expected go version, excluding `patch` version. Ex: 1.17",
    )
    args = parser.parse_args(argv)
    print("args", args)

    # get expected minimum go version
    reqVersion = args.version
    if reqVersion is None or not reqVersion.startswith("go"):
        return 1

    print("required version", reqVersion)

    # get go version
    stream = os.popen('go env GOVERSION')
    gotVersion = stream.read()

    if Version(gotVersion[2:]) < Version(reqVersion[2:]):
        print("need to upgrade go version to", reqVersion, "or more")
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
