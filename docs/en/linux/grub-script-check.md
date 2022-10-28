---
layout: page
title: linux/grub-script-check (English)
description: "The program `grub-script-check` takes a GRUB script file and checks it for syntax errors."
content_hash: 5ff8b4e00a62e139b3f6d9dc8ec7560ff8c16c5e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># grub-script-check

The program `grub-script-check` takes a GRUB script file and checks it for syntax errors.
It may take a path as a non-option argument. If none is supplied, it will read from standard input.
More information: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dscript_002dcheck.html>.

- Check a specific script file for syntax errors:

`grub-script-check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/grub_config_file</span>

- Display each line of input after reading it:

`grub-script-check --verbose`

- Display version:

`grub-script-check --version`

- Display help:

`grub-script-check --help`
