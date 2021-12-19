---
layout: page
title: common/meson (English)
description: "SCons-like build system that uses python as a front-end language and Ninja as a building backend."
content_hash: 08ccbc455d92e0a4598bad2a52d18690c7923c7b
---
# meson

SCons-like build system that uses python as a front-end language and Ninja as a building backend.
More information: <https://mesonbuild.com>.

- Generate a C project with a given name and version:

`meson init --language=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myproject</span>` --version=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>

- Configure the `builddir` with default values:

`meson setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build_dir</span>

- Build the project:

`meson compile -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_dir</span>

- Show the help:

`meson --help`

- Show version info:

`meson --version`
