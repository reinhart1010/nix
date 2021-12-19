---
layout: page
title: common/nm (English)
description: "List symbol names in object files."
content_hash: f5d0b58245837da165b48ff6fabe25c75f9a0059
---
# nm

List symbol names in object files.

- List global (extern) functions in a file (prefixed with T):

`nm -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.o</span>

- List only undefined symbols in a file:

`nm -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.o</span>

- List all symbols, even debugging symbols:

`nm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.o</span>

- Demangle C++ symbols (make them readable):

`nm --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.o</span>
