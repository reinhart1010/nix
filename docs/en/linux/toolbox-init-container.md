---
layout: page
title: linux/toolbox-init-container (English)
description: "Initialize a running `toolbox` container."
content_hash: 914433940d474e4335b53b91fa05fc12a24d57c1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox init-container

Initialize a running `toolbox` container.
This command is should not be executed by the user, and cannot be run on the host.
More information: <https://manned.org/toolbox-init-container.1>.

- Initialize a running toolbox:

`toolbox init-container --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gid</span>` --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">home</span>` --home-link --media-link --mnt-link --monitor-host --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>` --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
