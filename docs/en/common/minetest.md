---
layout: page
title: common/minetest (English)
description: "Multiplayer infinite-world block sandbox."
content_hash: cd056263a7d6488d3074b967554f1484461c578a
last_modified_at: 2024-10-02
related_topics:
  - title: Türkçe version
    url: /tr/common/minetest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minetest

Multiplayer infinite-world block sandbox.
See also `minetestserver`, the server-only binary.
More information: <https://wiki.minetest.org/Minetest>.

- Start Minetest in client mode:

`minetest`

- Start Minetest in server mode by hosting a specific world:

`minetest --server --world `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Write logs to a specific file:

`minetest --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Only write errors to the console:

`minetest --quiet`
