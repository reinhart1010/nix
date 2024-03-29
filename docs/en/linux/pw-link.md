---
layout: page
title: linux/pw-link (English)
description: "Manage links between ports in PipeWire."
content_hash: ca4bd8046e00c8782f91046a03cb5e16d683f9b8
last_modified_at: 2023-12-20
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-link.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-link.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-link

Manage links between ports in PipeWire.
More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- List all audio output and input ports with their IDs:

`pw-link --output --input --ids`

- Create a link between an output and an input port:

`pw-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- Disconnect two ports:

`pw-link --disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- List all links with their IDs:

`pw-link --links --ids`

- Display help:

`pw-link -h`
