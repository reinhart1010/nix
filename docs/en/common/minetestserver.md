---
layout: page
title: common/minetestserver (English)
description: "Multiplayer infinite-world block sandbox server."
content_hash: 5f05f81f647c96f4ca707f1b912083f6f9cdca1e
last_modified_at: 2024-01-24
related_topics:
  - title: Türkçe version
    url: /tr/common/minetestserver.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minetestserver

Multiplayer infinite-world block sandbox server.
See also `minetest`, the graphical client.
More information: <https://wiki.minetest.net/Setting_up_a_server>.

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
