---
layout: page
title: linux/ctrlaltdel (English)
description: "Utility to control what happens when CTRL+ALT+DEL is pressed."
content_hash: b26ccc41ffbe016e2a0cbd4541f258115a715cb7
---
# ctrlaltdel

Utility to control what happens when CTRL+ALT+DEL is pressed.

- Get current setting:

`ctrlaltdel`

- Set CTRL+ALT+DEL to reboot immediately, without any preparation:

`sudo ctrlaltdel hard`

- Set CTRL+ALT+DEL to reboot "normally", giving processes a chance to exit first (send SIGINT to PID1):

`sudo ctrlaltdel soft`
