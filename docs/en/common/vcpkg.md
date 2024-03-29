---
layout: page
title: common/vcpkg (English)
description: "Package manager for C/C++ libraries."
content_hash: 236894cf954841c9c9414b59b3632ccab7043d45
last_modified_at: 2024-02-20
tldri18n_status: 2
---
# vcpkg

Package manager for C/C++ libraries.
Note: packages are not installed in the system. To use them, you need to tell your build system (e.g. CMake) to use `vckg`.
More information: <https://learn.microsoft.com/en-us/vcpkg/>.

- Build and add package `libcurl` to the `vcpkg` environment:

`vcpkg install curl`

- Build and add `zlib` using the `emscripten` toolchain:

`vcpkg install --triplet=wasm32-emscripten zlib`

- Search for a package:

`vcpkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg_name</span>

- Configure a CMake project to use `vcpkg` packages:

`cmake -B build -DCMAKE_TOOLCHAIN_FILE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vcpkg_install_directory</span>`/scripts/buildsystems/vcpkg.cmake`
