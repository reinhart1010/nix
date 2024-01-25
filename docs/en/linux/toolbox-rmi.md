---
layout: page
title: linux/toolbox-rmi (English)
description: "Remove `toolbox` images."
content_hash: 4c3d165638d04fcedbd6f004ce44837562d80c6c
last_modified_at: 2024-01-25
related_topics:
  - title: தமிழ் version
    url: /ta/linux/toolbox-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox rmi

Remove `toolbox` images.
See also: `toolbox rm`.
More information: <https://manned.org/toolbox-rmi.1>.

- Remove one or more `toolbox` image:

`toolbox rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name1 image_name2 ...</span>

- Remove all `toolbox` images:

`toolbox rmi --all`

- Force the removal of a `toolbox` image which is currently being used by a container (the container will be removed as well):

`toolbox rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>
