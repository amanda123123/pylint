#!/usr/bin/env python

# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/pylint-dev/pylint/blob/main/LICENSE
# Copyright (c) https://github.com/pylint-dev/pylint/blob/main/CONTRIBUTORS.txt

import pylint
import os
os.mkdir(r"/tmp/dkfjd")
pylint.modify_sys_path()
pylint.run_pylint()
