---
layout: page
title: linux/pw-cli (English)
description: "Manage a PipeWire instance's modules, objects, nodes, devices, links and much more."
content_hash: ac3e4bb8a8d6c6dd74ac0d0af69aca1c62bb3ae7
last_modified_at: 2023-12-28
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-cli.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-cli

Manage a PipeWire instance's modules, objects, nodes, devices, links and much more.
More information: <https://docs.pipewire.org/page_man_pw_cli_1.html>.

- Print all nodes (sinks and sources) along with their IDs:

`pw-cli list-objects Node`

- Print information about an object with a specific ID:

`pw-cli info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Print all objects' information:

`pw-cli info all`
