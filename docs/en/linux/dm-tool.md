---
layout: page
title: linux/dm-tool (English)
description: "A tool to communicate with the display manager."
content_hash: 16560d457ccda7d6ae389044c5a80e9ada9016ff
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dm-tool

A tool to communicate with the display manager.
More information: <https://manned.org/dm-tool>.

- Show the greeter while keeping current desktop session open and waiting to be restored upon authentication by logged in user:

`dm-tool switch-to-greeter`

- Lock the current session:

`dm-tool lock`

- Switch to a specific user, showing an authentication prompt if required:

`dm-tool switch-to-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session</span>

- Add a dynamic seat from within a running LightDM session:

`dm-tool add-seat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xlocal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
