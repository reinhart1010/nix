---
layout: page
title: linux/pw-link (English)
description: "Manage links between ports in PipeWire."
content_hash: 1ee2b062bbb43cc98ec1ab874ac3769faecaa4c9
last_modified_at: 2022-12-16
related_topics:
  - title: Türkçe version
    url: /tr/linux/pw-link.html
    icon: bi bi-globe
---
# pw-link

Manage links between ports in PipeWire.
More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- List all audio output and input ports:

`pw-link --output --input`

- Create a link between an output and an input port:

`pw-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- Disconnect two ports:

`pw-link --disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- Display help:

`pw-link -h`
