---
layout: page
title: windows/vcvarsall (English)
description: "Setup the environment variables required for using the Microsoft Visual Studio tools from the command-line."
content_hash: 045b0e665f60f423ea3fcc1680595dc51aa856aa
last_modified_at: 2023-05-31
---
# vcvarsall

Setup the environment variables required for using the Microsoft Visual Studio tools from the command-line.
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
