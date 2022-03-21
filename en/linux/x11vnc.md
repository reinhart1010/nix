---
layout: page
title: linux/x11vnc (English)
description: "A VNC server that will enable VNC on an existing display server."
content_hash: 090e793bbe24a1455fda5feb5d0830dc14f115f1
---
# x11vnc

A VNC server that will enable VNC on an existing display server.
By default, the server will automatically terminate once all clients disconnect from it.
More information: <https://manned.org/x11vnc>.

- Launch a VNC server that allows multiple clients to connect:

`x11vnc -shared`

- Launch a VNC server in view-only mode, and which won't terminate once the last client disconnects:

`x11vnc -forever -viewonly`

- Launch a VNC server on a specific display and screen (both starting at index zero):

`x11vnc -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen</span>

- Launch a VNC server on the third display's default screen:

`x11vnc -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Launch a VNC server on the first display's second screen:

`x11vnc -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
