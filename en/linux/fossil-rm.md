---
layout: page
title: linux/fossil-rm (English)
description: "Remove files or directories from Fossil version control."
content_hash: 1917a0cf22618552dada35172e740fa3784c56a2
---
# fossil rm

Remove files or directories from Fossil version control.
See also `fossil forget`.
More information: <https://fossil-scm.org/home/help>.

- Remove a file or directory from Fossil version control:

`fossil rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Remove a file or directory from Fossil version control, and also delete it from the disk:

`fossil rm --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Re-add all previously removed and uncommitted files to Fossil version control:

`fossil rm --reset`
