---
layout: page
title: common/electron-packager (English)
description: "A tool used to build Electron app executables for Windows, Linux and macOS."
content_hash: e0981087fc8f689558b9473d817a728867bc1c4a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# electron-packager

A tool used to build Electron app executables for Windows, Linux and macOS.
Requires a valid package.json in the application directory.
More information: <https://github.com/electron/electron-packager>.

- Package an application for the current architecture and platform:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>`"`

- Package an application for all architectures and platforms:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>`" --all`

- Package an application for 64-bit Linux:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>`" --platform="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux</span>`" --arch="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x64</span>`"`

- Package an application for ARM macOS:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>`" --platform="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">darwin</span>`" --arch="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64</span>`"`
