---
layout: page
title: common/rabin2 (English)
description: "Get information about binary files (ELF, PE, Java CLASS, Mach-O) - symbols, sections, linked libraries, etc."
content_hash: e83b9c593012ba7d2d860afff56dc23033df4920
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rabin2

Get information about binary files (ELF, PE, Java CLASS, Mach-O) - symbols, sections, linked libraries, etc.
Comes bundled with `radare2`.
More information: <https://manned.org/rabin2>.

- Display general information about a binary (architecture, type, endianness):

`rabin2 -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display linked libraries:

`rabin2 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display symbols imported from libraries:

`rabin2 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display strings contained in the binary:

`rabin2 -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display the output in JSON:

`rabin2 -j -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
