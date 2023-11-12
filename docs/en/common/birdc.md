---
layout: page
title: common/birdc (English)
description: "Bird remote control."
content_hash: 1314aeea9bd6ef62d7bf0f4e8b948057bdef06fe
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/birdc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# birdc

Bird remote control.
Command tool to retrieve information like routes from bird and perform configurations during runtime.
More information: <https://bird.network.cz/>.

- Open the remote control console:

`birdc`

- Reload the configuration without restarting Bird:

`birdc configure`

- Show the current status of Bird:

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
