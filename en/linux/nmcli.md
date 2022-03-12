---
layout: page
title: linux/nmcli (English)
description: "A command-line tool for controlling NetworkManager."
content_hash: b5c739475f85fc5403bac591526f3ae211b6baba
related_topics:
  - title: മലയാളം version
    url: /ml/linux/nmcli.html
    icon: bi bi-globe
---
# nmcli

A command-line tool for controlling NetworkManager.
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
