---
layout: page
title: linux/pivpn (English)
description: "Easy security-hardened OpenVPN setup and manager."
content_hash: 81961f2f189a621dcdf998d66e9a060643a7b1a7
---
# pivpn

Easy security-hardened OpenVPN setup and manager.
Originally designed for the Raspberry Pi, but works on other Linux devices too.
More information: <http://www.pivpn.io/>.

- Add a new client device:

`sudo pivpn add`

- List all client devices:

`sudo pivpn list`

- List currently connected devices and their statistics:

`sudo pivpn clients`

- Revoke a previously authenticated device:

`sudo pivpn revoke`

- Uninstall PiVPN:

`sudo pivpn uninstall`
