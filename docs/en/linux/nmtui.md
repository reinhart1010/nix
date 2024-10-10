---
layout: page
title: linux/nmtui (English)
description: "Text user interface for controlling NetworkManager."
content_hash: 2d4f821e62643e58ddad8c74b5e79aa392d17eef
last_modified_at: 2024-10-10
related_topics:
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmtui.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmtui.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmtui

Text user interface for controlling NetworkManager.
Use arrow keys to navigate, enter to select an option.
More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Open the user interface:

`nmtui`

- List available connections, with the option to activate or deactivate them:

`nmtui connect`

- Connect to a given network:

`nmtui connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid|device|SSID</span>

- Edit/Add/Delete a given network:

`nmtui edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|id</span>

- Set the system hostname:

`nmtui hostname`
