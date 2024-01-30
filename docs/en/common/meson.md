---
layout: page
title: common/meson (English)
description: "SCons-like build system that uses Python as a front-end language and Ninja as a building backend."
content_hash: 001f56c2aa87d4e5daece0b270cdbe1e96b72504
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# meson

SCons-like build system that uses Python as a front-end language and Ninja as a building backend.
More information: <https://mesonbuild.com>.

- Generate a C project with a given name and version:

`meson init --language=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myproject</span>` --version=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>

- Configure the `builddir` with default values:

`meson setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build_dir</span>

- Build the project:

`meson compile -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_dir</span>

- Run all tests in the project:

`meson test`

- Show the help:

`meson --help`

- Display version:

`meson --version`
