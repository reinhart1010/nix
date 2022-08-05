---
layout: page
title: linux/toolbox-rmi (English)
description: "Remove one or more `toolbox` images."
content_hash: f52577ffa68d3b4d01862a38530cb14f58174e2a
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox rmi

Remove one or more `toolbox` images.
See also: `toolbox rm`.
More information: <https://manned.org/toolbox-rmi.1>.

- Remove a `toolbox` image:

`toolbox rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Remove all `toolbox` images:

`toolbox rmi --all`

- Force the removal of a `toolbox` image which is currently being used by a container (the container will be removed as well):

`toolbox rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>
