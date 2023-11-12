---
layout: page
title: linux/genisoimage (English)
description: "Pre-mastering program to generate ISO9660/Joliet/HFS hybrid filesystems."
content_hash: 790fc941eb5c5d9cd69f8650de555e3995e959e7
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/genisoimage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# genisoimage

Pre-mastering program to generate ISO9660/Joliet/HFS hybrid filesystems.
More information: <https://manpages.debian.org/latest/genisoimage/genisoimage.1.en.html>.

- Create an ISO image from the given source directory:

`genisoimage -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myimage.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>

- Create an ISO image with files larger than 2GiB by reporting a smaller apparent size for ISO9660 filesystems:

`genisoimage -o -allow-limited-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myimage.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>
