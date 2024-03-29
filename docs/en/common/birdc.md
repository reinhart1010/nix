---
layout: page
title: common/birdc (English)
description: "BIRD remote control."
content_hash: 24362ecf296c3e6b012203af6913796fa63bce9e
last_modified_at: 2024-02-15
related_topics:
  - title: Deutsch version
    url: /de/common/birdc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# birdc

BIRD remote control.
Retrieve information like routes from bird and perform configurations during runtime.
More information: <https://bird.network.cz/>.

- Open the remote control console:

`birdc`

- Reload the configuration without restarting BIRD:

`birdc configure`

- Show the current status of BIRD:

`birdc show status`

- Show all configured protocols:

`birdc show protocols`

- Show all details about a protocol:

`birdc show protocols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upstream1</span>` all`

- Show all routes that contain a specific AS number:

`birdc "show route where bgp_path ~ [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4242120045</span>`]"`

- Show all best routes:

`birdc show route primary`

- Show all details of all routes from a given prefix:

`birdc show route for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fd00:/8</span>` all`
