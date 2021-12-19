---
layout: page
title: linux/iwctl (English)
description: "A command-line tool for controlling the iwd network supplicant."
content_hash: de79efe4675e926541c7a3bc88bdf2c9a954f547
related_topics:
  - title: français version
    url: /fr/linux/iwctl.html
    icon: bi bi-globe
---
# iwctl

A command-line tool for controlling the iwd network supplicant.
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
