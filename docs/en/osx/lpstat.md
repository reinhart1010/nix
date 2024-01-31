---
layout: page
title: osx/lpstat (English)
description: "Display status information about the current classes, jobs, and printers."
content_hash: 79ef3c1c4f2c34bc77acbc15df3130c3ad6d9b4d
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# lpstat

Display status information about the current classes, jobs, and printers.
More information: <https://keith.github.io/xcode-man-pages/lpstat.1.html>.

- Show a long listing of printers, classes, and jobs:

`lpstat -l`

- Force encryption when connecting to the CUPS server:

`lpstat -E`

- Show the ranking of print jobs:

`lpstat -R`

- Show whether or not the CUPS server is running:

`lpstat -r`

- Show all status information:

`lpstat -t`
