---
layout: page
title: linux/nmcli (English)
description: "A command-line tool for controlling NetworkManager."
content_hash: de067a16a5fce3115f7339f6918ad56ddb0a1fd0
related_topics:
  - title: മലയാളം version
    url: /ml/linux/nmcli.html
    icon: bi bi-globe
---
# nmcli

A command-line tool for controlling NetworkManager.
Some subcommands such as `nmcli monitor` have their own usage documentation.
More information: <https://manned.org/nmcli>.

- Run an `nmcli` subcommand:

`nmcli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent|connection|device|general|help|monitor|networking|radio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_options</span>

- Display the current version of NetworkManager:

`nmcli --version`

- Display help:

`nmcli --help`

- Display help for a subcommand:

`nmcli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
