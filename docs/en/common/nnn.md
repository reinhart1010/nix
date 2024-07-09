---
layout: page
title: common/nnn (English)
description: "Interactive terminal file manager and disk usage analyzer."
content_hash: 29818d93502a041aa8610e44ef63a5b694281681
last_modified_at: 2024-07-09
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
