---
layout: page
title: common/xmake (English)
description: "A cross-platform C & C++ build utility based on Lua."
content_hash: 24d3a5d1c1822bc966e483be6b1220655b714777
last_modified_at: 2024-07-05
tldri18n_status: 2
---
# xmake

A cross-platform C & C++ build utility based on Lua.
More information: <https://xmake.io/#/getting_started>.

- Create an Xmake C project, consisting of a hello world and `xmake.lua`:

`xmake create --language c -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Build and run an Xmake project:

`xmake build run`

- Run a compiled Xmake target directly:

`xmake run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>

- Configure a project's build targets:

`xmake config --plat=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macosx|linux|iphoneos|...</span>` --arch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64|i386|arm64|...</span>` --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|release</span>

- Install the compiled target to a directory:

`xmake install -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
