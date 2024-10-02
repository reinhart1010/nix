---
layout: page
title: common/minetestserver (English)
description: "Multiplayer infinite-world block sandbox server."
content_hash: d46270883a7f35aa09f19415f08c7a65bbbc9b2c
last_modified_at: 2024-10-02
related_topics:
  - title: Türkçe version
    url: /tr/common/minetestserver.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minetestserver

Multiplayer infinite-world block sandbox server.
See also `minetest`, the graphical client.
More information: <https://wiki.minetest.org/Setting_up_a_server>.

- Start the server:

`minetestserver`

- List available worlds:

`minetestserver --world list`

- Load the specified world:

`minetestserver --world `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">world_name</span>

- List the available game IDs:

`minetestserver --gameid list`

- Use the specified game:

`minetestserver --gameid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">game_id</span>

- Listen on a specific port:

`minetestserver --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">34567</span>

- Migrate to a different data backend:

`minetestserver --migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqlite3|leveldb|redis</span>

- Start an interactive terminal after starting the server:

`minetestserver --terminal`
