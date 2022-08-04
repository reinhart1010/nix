---
layout: page
title: common/piactl (English)
description: "The command-line tool for Private Internet Access, a commercial VPN provider."
content_hash: 70cf7a8ac294b6beee2072f48d1de06aa3cb95ae
---
# piactl

The command-line tool for Private Internet Access, a commercial VPN provider.
More information: <https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-part-1>.

- Log in to Private Internet Access:

`piactl login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/login_file</span>

- Connect to Private Internet Access:

`piactl connect`

- Disconnect from Private Internet Access:

`piactl disconnect`

- Enable or disable the Private Internet Access daemon in the background:

`piactl background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- List all available VPN regions:

`piactl get regions`

- Display the current VPN region:

`piactl get region`

- Set your VPN region:

`piactl set region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>

- Log out of Private Internet Access:

`piactl logout`
