---
layout: page
title: common/birdc (English)
description: "Bird remote control."
content_hash: 5e6853fe5a51f76598dfd0cde79ad898f06c0a51
last_modified_at: 2023-03-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># birdc

Bird remote control.
Command tool to retrieve information like routes from bird and perform configurations during runtime.
More information: <https://bird.network.cz/>.

- Open the remote control console::

`birdc`

- Reload the configuration without restarting Bird:

`birdc configure`

- Show the current status of Bird:

`birdc show status`

- Show all active protocols:

`birdc show protocols`

- Show all details about a protocol:

`birdc show protocols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upstream1</span>` all`

- Show all routes that contain a specific AS number:

`birdc "show route where bgp_path ~ [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4242120045</span>`]"`

- Show all best routes:

`birdc show route primary`

- Show all details of all routes from a given prefix:

`birdc show route for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fd00:/8</span>` all`
