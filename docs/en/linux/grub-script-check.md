---
layout: page
title: linux/grub-script-check (English)
description: "The program `grub-script-check` takes a GRUB script file and checks it for syntax errors."
content_hash: 68e68cf58b762040115cd0641254198b832fe956
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# grub-script-check

The program `grub-script-check` takes a GRUB script file and checks it for syntax errors.
It may take a path as a non-option argument. If none is supplied, it will read from `stdin`.
More information: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dscript_002dcheck.html>.

- Check a specific script file for syntax errors:

`grub-script-check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/grub_config_file</span>

- Display each line of input after reading it:

`grub-script-check --verbose`

- Display version:

`grub-script-check --version`

- Display help:

`grub-script-check --help`
