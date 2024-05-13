---
layout: page
title: linux/readelf (English)
description: "Display information about ELF files."
content_hash: a1eba4a0b9b968a2dc10d158802de591ca5630c6
last_modified_at: 2024-05-13
related_topics:
  - title: 中文 version
    url: /zh/linux/readelf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# readelf

Display information about ELF files.
More information: <https://manned.org/readelf.1>.

- Display all information about the ELF file:

`readelf -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display all the headers present in the ELF file:

`readelf --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the entries in symbol table section of the ELF file, if it has one:

`readelf --symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display ELF header information:

`readelf --file-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display ELF section header information:

`readelf --section-headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
