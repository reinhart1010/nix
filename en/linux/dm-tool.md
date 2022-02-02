---
layout: page
title: linux/dm-tool (English)
description: "A tool to communicate with the display manager."
content_hash: cf5918b9cf7e3f3211533d687d84f37f8c5fa1f3
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dm-tool

A tool to communicate with the display manager.
More information: <https://manned.org/dm-tool>.

- Show the greeter while keeping current desktop session open and waiting to be restored upon authentication by logged in user:

`dm-tool switch-to-greeter`

- Lock the current session:

`dm-tool lock`

- Swicth to a specific user, showing an authentication prompt if required:

`dm-tool switch-to-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session</span>

- Add a dynamic seat from within a running LightDM session:

`dm-tool add-seat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xlocal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
