---
layout: page
title: linux/x0vncserver (English)
description: "TigerVNC Server for X displays."
content_hash: 82ff2f62ec86f48d83cacee02a1625d6bbadfb62
---
# x0vncserver

TigerVNC Server for X displays.
More information: <https://tigervnc.org/doc/x0vncserver.html>.

- Start a VNC server using a passwordfile:

`x0vncserver -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:0</span>` -passwordfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start a VNC server using a specific port:

`x0vncserver -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:0</span>` -rfbport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>
