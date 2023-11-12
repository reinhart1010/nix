---
layout: page
title: windows/vcvarsall (English)
description: "Setup the environment variables required for using the Microsoft Visual Studio tools."
content_hash: 2d0e79a7137f59153c5c5d6c36eaae6da873ec35
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vcvarsall

Setup the environment variables required for using the Microsoft Visual Studio tools.
The path of `vcvarsall` for a certain Visual Studio installation can be found using `vswhere`.
More information: <https://learn.microsoft.com/cpp/build/building-on-the-command-line>.

- Setup the environment for native x64:

`vcvarsall x64`

- Setup the environment for cross-compiled native x86 from the x64 host:

`vcvarsall x64_x86`

- Setup the environment for cross-compiled native Arm x64 from the x64 host:

`vcvarsall x64_arm64`

- Setup the environment for native UWP x64:

`vcvarsall x64 uwp`
