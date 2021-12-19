---
layout: page
title: common/nice (English)
description: "Execute a program with a custom scheduling priority (niceness)."
content_hash: d55d44dc2782770d88134fcb4212164e4ed95f75
---
# nice

Execute a program with a custom scheduling priority (niceness).
Niceness values range from -20 (the highest priority) to 19 (the lowest).
More information: <https://www.gnu.org/software/coreutils/nice>.

- Launch a program with altered priority:

`nice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
