#!/usr/bin/env python3
"""Builds docs/ (GitHub Pages root). The code lives in qc/; see qc/build.py for inputs
and EDITORIAL.md for how to write a change. Standard library only.

  python3 build_site.py                    # build (pings IndexNow)
  QC_NO_INDEXNOW=1 python3 build_site.py   # build without pinging
"""
import sys
from qc.build import main

if __name__ == "__main__":
    sys.exit(main())
