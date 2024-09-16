---
layout: page
title: common/nnn (English)
description: "Interactive terminal file manager and disk usage analyzer."
content_hash: ddc6c9d8666993672ea35ff83385e795c3f9760d
last_modified_at: 2024-09-16
related_topics:
  - title: español version
    url: /es/common/nnn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nnn

Interactive terminal file manager and disk usage analyzer.
More information: <https://github.com/jarun/nnn>.

- Open the current directory (or specify one as the first argument):

`nnn`

- Start in detailed mode:

`nnn -d`

- Show hidden files:

`nnn -H`

- Open an existing bookmark (defined in the `NNN_BMS` environment variable):

`nnn -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bookmark_name</span>

- Sort files on [a]pparent disk usage / [d]isk usage / [e]xtension / [r]everse / [s]ize / [t]ime / [v]ersion:

`nnn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|d|e|r|s|t|v</span>

- Open a file you have selected. Select the file then press `o`, and type a program to open the file in:

`nnn -o`
