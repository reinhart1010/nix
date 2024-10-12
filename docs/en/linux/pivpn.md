---
layout: page
title: linux/pivpn (English)
description: "Easy security-hardened OpenVPN setup and manager."
content_hash: 2d5d76bc426575e5a48aa36d16199e73e55b741c
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# pivpn

Easy security-hardened OpenVPN setup and manager.
Originally designed for the Raspberry Pi, but works on other Linux devices too.
More information: <https://www.pivpn.io/>.

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
