---
layout: page
title: osx/lpstat (English)
description: "Display status information about the current classes, jobs, and printers."
content_hash: 6b0c7ae0875860d9cad6413f902838378181dbb0
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lpstat

Display status information about the current classes, jobs, and printers.
More information: <https://ss64.com/osx/lpstat.html>.

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
