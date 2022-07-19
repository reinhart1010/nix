---
layout: page
title: linux/ctr (English)
description: "Manage `containerd` containers and images."
content_hash: 282e3a90f206a4c6e97a1243f4e192d8cb5cfe60
---
# ctr

Manage `containerd` containers and images.
More information: <https://containerd.io>.

- List all containers (running and stopped):

`ctr containers list`

- List all images:

`ctr images list`

- Pull an image:

`ctr images pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Tag an image:

`ctr images tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_tag</span>
