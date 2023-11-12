---
layout: page
title: common/pio-ci (English)
description: "Build PlatformIO projects with an arbitrary source code structure."
content_hash: ebecb3ddf46dda252ce59fa64bfc1c83ecbf9ce8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pio ci

Build PlatformIO projects with an arbitrary source code structure.
This will create a new temporary project which the source code will be copied into.
More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>.

- Build a PlatformIO project in the default system temporary directory and delete it afterwards:

`pio ci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- Build a PlatformIO project and specify specific libraries:

`pio ci --lib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- Build a PlatformIO project and specify a specific board (`pio boards` lists all of them):

`pio ci --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">board</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- Build a PlatformIO project in a specific directory:

`pio ci --build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- Build a PlatformIO project and don't delete the build directory:

`pio ci --keep-build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- Build a PlatformIO project using a specific configuration file:

`pio ci --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/platformio.ini</span>
