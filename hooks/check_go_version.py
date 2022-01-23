from __future__ import annotations

import os
import re
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    stream = os.popen('go env GOVERSION')
    output = stream.read()
    x = re.search("go1.17.*", output)
    if x:
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
