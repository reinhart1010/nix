---
layout: page
title: common/objdump (English)
description: "View information about object files."
content_hash: 5f34dac4062d25b8117436c099888d02ec475753
last_modified_at: 2024-11-28
related_topics:
  - title: español version
    url: /es/common/objdump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/objdump.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/objdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# objdump

View information about object files.
More information: <https://manned.org/objdump>.

- Display the file header information:

`objdump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display all header information:

`objdump -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the disassembled output of executable sections:

`objdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the disassembled executable sections in Intel syntax:

`objdump -M intel -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display a complete binary hex dump of all sections:

`objdump -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
