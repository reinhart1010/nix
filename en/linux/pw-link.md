---
layout: page
title: linux/pw-link (English)
description: "Manage links between ports in PipeWire."
content_hash: 173e300bb6258596ba9c521d42db4b9e136d9bc0
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-link

Manage links between ports in PipeWire.
More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- List all audio output and input ports:

`pw-link --output --input'`

- Create a link between an output and an input port:

`pw-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- Disconnect two ports:

`pw-link --disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- Display help:

`pw-link -h`
