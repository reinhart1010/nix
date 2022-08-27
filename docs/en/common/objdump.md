---
layout: page
title: common/objdump (English)
description: "View information about object files."
content_hash: 73f43ea0c9a56a544fd2ce013073d7a7683b9f49
---
# objdump

View information about object files.
More information: <https://manned.org/objdump>.

- Display the file header information:

`objdump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Display the disassembled output of executable sections:

`objdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Display the disassembled executable sections in intel syntax:

`objdump -M intel -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Display a complete binary hex dump of all sections:

`objdump -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>
