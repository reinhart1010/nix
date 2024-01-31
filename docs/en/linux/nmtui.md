---
layout: page
title: linux/nmtui (English)
description: "Text user interface for controlling NetworkManager."
content_hash: 8101dcbbda905f18d618bf0e7175aa35c810994a
last_modified_at: 2024-01-31
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
More information: <https://networkmanager.dev/docs/api/latest/nmtui.html>.

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
