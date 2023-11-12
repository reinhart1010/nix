---
layout: page
title: linux/toolbox-rmi (English)
description: "Remove one or more `toolbox` images."
content_hash: f52577ffa68d3b4d01862a38530cb14f58174e2a
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/linux/toolbox-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox rmi

Remove one or more `toolbox` images.
See also: `toolbox rm`.
More information: <https://manned.org/toolbox-rmi.1>.

- Remove a `toolbox` image:

`toolbox rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Remove all `toolbox` images:

`toolbox rmi --all`

- Force the removal of a `toolbox` image which is currently being used by a container (the container will be removed as well):

`toolbox rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>
