---
layout: page
title: linux/nmcli (English)
description: "Manage the network configuration using NetworkManager."
content_hash: c1ca7a4fad7822c6b64c7ae79eafe22b8d4570fe
last_modified_at: 2023-07-16
related_topics:
  - title: മലയാളം version
    url: /ml/linux/nmcli.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmcli.html
    icon: bi bi-globe
---
# nmcli

Manage the network configuration using NetworkManager.
Some subcommands such as `nmcli monitor` have their own usage documentation.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Run an `nmcli` subcommand:

`nmcli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent|connection|device|general|help|monitor|networking|radio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_options</span>

- Display the current version of NetworkManager:

`nmcli --version`

- Display help:

`nmcli --help`

- Display help for a subcommand:

`nmcli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
