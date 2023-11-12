---
layout: page
title: linux/iwctl (English)
description: "Control the `iwd` network supplicant."
content_hash: bb0c2358cc72df42ec1e505b7ad740f621f2c8d7
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/iwctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iwctl

Control the `iwd` network supplicant.
More information: <https://iwd.wiki.kernel.org/gettingstarted>.

- Start the interactive mode, in this mode you can enter the commands directly, with autocompletion:

`iwctl`

- Call general help:

`iwctl --help`

- Display your Wi-Fi stations:

`iwctl station list`

- Start looking for networks with a station:

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">station</span>` scan`

- Display the networks found by a station:

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">station</span>` get-networks`

- Connect to a network with a station, if credentials are needed they will be asked:

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">station</span>` connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>
