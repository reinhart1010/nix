---
layout: page
title: linux/ldd (English)
description: "Display shared library dependencies of a binary."
content_hash: 7cb436d54b48721f225cfc85c450c0df66bf45bf
related_topics:
  - title: Deutsch version
    url: /de/linux/ldd.html
    icon: bi bi-globe
---
# ldd

Display shared library dependencies of a binary.
Do not use on an untrusted binary, use objdump for that instead.
More information: <https://manned.org/ldd>.

- Display shared library dependencies of a binary:

`ldd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display all information about dependencies:

`ldd --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display unused direct dependencies:

`ldd --unused `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Report missing data objects and perform data relocations:

`ldd --data-relocs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Report missing data objects and functions, and perform relocations for both:

`ldd --function-relocs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
