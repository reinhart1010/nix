---
layout: page
title: linux/readelf (English)
description: "Display information about ELF files."
content_hash: d1a60498452112781fdc8a46eedcd0f8e69b2117
last_modified_at: 2024-04-18
related_topics:
  - title: 中文 version
    url: /zh/linux/readelf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# readelf

Display information about ELF files.
More information: <http://man7.org/linux/man-pages/man1/readelf.1.html>.

- Display all information about the ELF file:

`readelf -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display all the headers present in the ELF file:

`readelf --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the entries in symbol table section of the ELF file, if it has one:

`readelf --symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the information contained in the ELF header at the start of the file:

`readelf --file-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
