---
layout: page
title: linux/steamos-session-select (English)
description: "Manipulate which session is currently in use."
content_hash: 71e6bc0a9fc035b22b53bf00f3a653823276af91
last_modified_at: 2024-12-26
related_topics:
  - title: 한국어 version
    url: /ko/linux/steamos-session-select.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steamos-session-select

Manipulate which session is currently in use.
More information: <https://gitlab.com/users/evlaV/projects>.

- Change to desktop mode:

`steamos-session-select plasma`

- Change to gamemode (sets the system to boot into gamemode if `-persistent` options were selected previously):

`steamos-session-select`

- Change to Wayland desktop mode:

`steamos-session-select plasma-wayland`

- Change to Wayland desktop mode and have the device boot to desktop:

`steamos-session-select plasma-wayland-persistent`

- Change to X11 desktop mode and have the device boot to desktop:

`steamos-session-select plasma-x11-persistent`
