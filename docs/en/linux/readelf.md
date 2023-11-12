---
layout: page
title: linux/readelf (English)
description: "Displays information about ELF files."
content_hash: f7c4a90561eb7a708da8511e835db32242a35004
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/readelf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# readelf

Displays information about ELF files.
More information: <http://man7.org/linux/man-pages/man1/readelf.1.html>.

- Display all information about the ELF file:

`readelf -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display all the headers present in the ELF file:

`readelf --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the entries in symbol table section of the ELF file, if it has one:

`readelf --symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the information contained in the ELF header at the start of the file:

`readelf --file-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
