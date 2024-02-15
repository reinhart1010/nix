---
layout: page
title: osx/lipo (English)
description: "Handle Mach-O Universal Binaries."
content_hash: 8ab7174c24803212ac42b899636d1b585395f50e
last_modified_at: 2024-02-15
related_topics:
  - title: español version
    url: /es/osx/lipo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/lipo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lipo

Handle Mach-O Universal Binaries.
More information: <https://keith.github.io/xcode-man-pages/lipo.1.html>.

- Create a universal file from two single-architecture files:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file.x86_64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file.arm64e</span>` -create -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>

- List all architectures contained in a universal file:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>` -archs`

- Display detailed information about a universal file:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>` -detailed_info`

- Extract a single-architecture file from a universal file:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file</span>` -thin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64e</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_file.arm64e</span>
