---
layout: page
title: linux/ctrlaltdel (English)
description: "Utility to control what happens when CTRL+ALT+DEL is pressed."
content_hash: 81b7f57c9e0c5b497a23df4e7885132e7c1a7150
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ctrlaltdel

Utility to control what happens when CTRL+ALT+DEL is pressed.
More information: <https://manned.org/ctrlaltdel>.

- Get current setting:

`ctrlaltdel`

- Set CTRL+ALT+DEL to reboot immediately, without any preparation:

`sudo ctrlaltdel hard`

- Set CTRL+ALT+DEL to reboot "normally", giving processes a chance to exit first (send SIGINT to PID1):

`sudo ctrlaltdel soft`
