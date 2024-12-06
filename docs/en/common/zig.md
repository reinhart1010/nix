---
layout: page
title: common/zig (English)
description: "The Zig compiler and toolchain."
content_hash: 77cec0d65804f9bdbab97c92a98b4a6a99449ba9
last_modified_at: 2024-12-06
related_topics:
  - title: 한국어 version
    url: /ko/common/zig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zig

The Zig compiler and toolchain.
More information: <https://ziglang.org>.

- Compile the project in the current directory:

`zig build`

- Compile and run the project in the current directory:

`zig build run`

- Initialize a `zig build` project with library and executable:

`zig init`

- Create and run a test build:

`zig test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zig</span>

- Cross compile, build and run a project for `x86_64` architecture and `windows` operating system:

`zig build run -fwine -Dtarget=x86_64-windows`

- Reformat Zig source into canonical form:

`zig fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zig</span>

- Translate a C file to `zig`:

`zig translate-c -lc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.c</span>

- Use Zig as a drop-in C++ compiler:

`zig c++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>
