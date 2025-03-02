---
layout: page
title: common/vdir (English)
description: "List directory contents."
content_hash: f306aaddcf87005caaf95562df9585d437986f68
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/vdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vdir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vdir

List directory contents.
Drop-in replacement for `ls -l`.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/vdir-invocation.html>.

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
