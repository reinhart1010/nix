---
layout: page
title: linux/kdocker (English)
description: "Easily dock applications to the system tray."
content_hash: a7673b2181dca8524f4dfa152a8c77aad72a42ae
---
# kdocker

Easily dock applications to the system tray.
More information: <https://github.com/user-none/KDocker>.

- Display a cursor to send a window to the system tray when pressing the left mouse button (press any other mouse button to cancel):

`kdocker`

- Open an application and send it to the system tray:

`kdocker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>

- Send focused window to the system tray:

`kdocker -f`

- Display a cursor to send a window to the system tray with a custom icon when pressing the left mouse button:

`kdocker -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/icon</span>

- Open an application, send it to the system tray and if focus is lost, minimize it:

`kdocker -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>

- Print version:

`kdocker --version`
