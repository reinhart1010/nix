---
layout: page
title: linux/nmcli-general (English)
description: "Manage general settings of NetworkManager."
content_hash: 6d625e7fba90183d17a93ddb72778dd3b13fd8ef
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/linux/nmcli-general.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli general

Manage general settings of NetworkManager.
This subcommand can also be called with `nmcli g`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Show the general status of NetworkManager:

`nmcli general`

- Show the hostname of the current device:

`nmcli general hostname`

- Change the hostname of the current device:

`sudo nmcli general hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_hostname</span>

- Show the permissions of NetworkManager:

`nmcli general permissions`

- Show the current logging level and domains:

`nmcli general logging`

- Set the logging level and/or domains (see `man NetworkManager.conf` for all available domains):

`nmcli general logging level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INFO|OFF|ERR|WARN|DEBUG|TRACE</span>` domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_1,domain_2,...</span>
