---
layout: page
title: linux/getcap (English)
description: "Command to display the name and capabilities of each specified file."
content_hash: 8511c003def22fbe737d4724a196bfa401fa8494
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># getcap

Command to display the name and capabilities of each specified file.
More information: <https://manned.org/getcap>.

- Get capabilities for the given files:

`getcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Displays all searched entries even if no capabilities are set:

`getcap -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
