#!/usr/bin/env python
# Example Device Under Test

import sys

if __name__ == "__main__":
	argv = sys.argv
	argv.pop(0)
	for arg in argv:
		print arg