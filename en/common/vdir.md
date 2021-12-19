---
layout: page
title: common/vdir (English)
description: "List directory contents."
content_hash: 54ea4ae4aac636b93ed127f9a06bc2b6efe6ebb9
---
# vdir

List directory contents.
Drop-in replacement for `ls -l`.
More information: <https://www.gnu.org/software/coreutils/vdir>.

- List files and directories in the current directory, one per line, with details:

`vdir`

- List with sizes displayed in human-readable units (KB, MB, GB):

`vdir -h`

- List including hidden files (starting with a dot):

`vdir -a`

- List files and directories sorting entries by size (largest first):

`vdir -S`

- List files and directories sorting entries by modification time (newest first):

`vdir -t`

- List grouping directories first:

`vdir --group-directories-first`

- Recursively list all files and directories in a specific directory:

`vdir --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
