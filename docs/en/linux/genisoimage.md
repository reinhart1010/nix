---
layout: page
title: linux/genisoimage (English)
description: "Pre-mastering program to generate ISO9660/Joliet/HFS hybrid filesystems."
content_hash: 9143fd5a686af39faeaf2f2d35e46d058e8aed85
last_modified_at: 2024-09-18
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/genisoimage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# genisoimage

Pre-mastering program to generate ISO9660/Joliet/HFS hybrid filesystems.
More information: <https://manned.org/genisoimage.1>.

- Create an ISO image from the given source directory:

`genisoimage -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myimage.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>

- Create an ISO image with files larger than 2GiB by reporting a smaller apparent size for ISO9660 filesystems:

`genisoimage -o -allow-limited-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myimage.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>
