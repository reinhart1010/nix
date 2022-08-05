---
layout: page
title: linux/toolbox-rm (English)
description: "Remove one or more `toolbox` containers."
content_hash: bc3baffb0af235a34d4d3be77605232eba3f3fa2
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox rm

Remove one or more `toolbox` containers.
See also: `toolbox rmi`.
More information: <https://manned.org/toolbox-rm.1>.

- Remove a toolbox container:

`toolbox rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Remove all `toolbox` containers:

`toolbox rm --all`

- Force the removal of a currently active `toolbox` container:

`toolbox rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
