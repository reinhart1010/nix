---
layout: page
title: common/pfetch (English)
description: "Display system information."
content_hash: ad458feb4bc05234a0215d3aa225b9073e91a20c
---
# pfetch

Display system information.
More information: <https://github.com/dylanaraps/pfetch>.

- Display the ASCII art and default fields:

`pfetch`

- Display only the ASCII art and color palette fields:

`PF_INFO="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ascii palette</span>`" pfetch`

- Display all possible fields:

`PF_INFO="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ascii title os host kernel uptime pkgs memory shell editor wm de palette</span>`" pfetch`

- Display a different username and hostname:

`USER="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`" HOSTNAME="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`" pfetch`

- Display without colors:

`PF_COLOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` pfetch`
