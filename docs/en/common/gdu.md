---
layout: page
title: common/gdu (English)
description: "Disk usage analyzer with console interface."
content_hash: 3b9f041a9fcb16ba75e8e956647598767e2e7683
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/gdu.html
    icon: bi bi-globe
---
# gdu

Disk usage analyzer with console interface.
More information: <https://github.com/dundee/gdu>.

- Interactively show the disk usage of the current directory:

`gdu`

- Interactively show the disk usage of a given directory:

`gdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Interactively show the disk usage of all mounted disks:

`gdu --show-disks`

- Interactively show the disk usage of the current directory but ignore some sub-directories:

`gdu --ignore-dirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1,path/to/directory2,...</span>

- Ignore paths by regular expression:

`gdu --ignore-dirs-pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.*[abc]+</span>`'`

- Ignore hidden directories:

`gdu --no-hidden`

- Only print the result, do not enter interactive mode:

`gdu --non-interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Do not show the progress in non-interactive mode (useful in scripts):

`gdu --no-progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
