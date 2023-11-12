---
layout: page
title: linux/size (English)
description: "Displays the sizes of sections inside binary files."
content_hash: 72d98096033d6b8ea9cfeeae3d8e1883b2a0eead
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# size

Displays the sizes of sections inside binary files.
More information: <https://sourceware.org/binutils/docs/binutils/size.html>.

- Display the size of sections in a given object or executable file:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the size of sections in a given object or executable file in [o]ctal:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--radix=8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the size of sections in a given object or executable file in [d]ecimal:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--radix=10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the size of sections in a given object or executable file in he[x]adecimal:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--radix=16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
