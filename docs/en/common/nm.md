---
layout: page
title: common/nm (English)
description: "List symbol names in object files."
content_hash: 02a5e43cba5259afbb3acde20e580a8abda05d8c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nm

List symbol names in object files.
More information: <https://manned.org/nm>.

- List global (extern) functions in a file (prefixed with T):

`nm -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>

- List only undefined symbols in a file:

`nm -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>

- List all symbols, even debugging symbols:

`nm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>

- Demangle C++ symbols (make them readable):

`nm --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>
