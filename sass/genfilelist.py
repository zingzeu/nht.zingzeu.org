#!/usr/bin/env python3

import glob

scssFiles = glob.glob("node_modules/bootstrap/scss/**/*.scss",recursive=True)

for f in scssFiles:
    print("\"@npm//:"+f+"\",")