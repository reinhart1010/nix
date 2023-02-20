---
layout: page
title: osx/lipo (English)
description: "Tool for handling Mach-O Universal Binaries."
content_hash: 5c6023fed0b1a95291176ab663d5eff4116cce7d
last_modified_at: 2023-02-20
---
# lipo

Tool for handling Mach-O Universal Binaries.
More information: <https://ss64.com/osx/lipo.html>.

- Create a universal file from two single-architecture files:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file.x86_64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file.arm64e</span>` -create -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>

- List all architectures contained in a universal file:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>` -archs`

- Display detailed information about a universal file:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>` -detailed_info`

- Extract a single-architecture file from a universal file:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>` -thin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64e</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file.arm64e</span>
