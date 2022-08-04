---
layout: page
title: linux/nmtui (English)
description: "Text user interface for controlling NetworkManager."
content_hash: 84e774b68f058214e43e09621d6d104850441e32
related_topics:
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
---
# nmtui

Text user interface for controlling NetworkManager.
Use arrow keys to navigate, enter to select an option.
More information: <https://networkmanager.dev/docs/api/latest/nmtui.html>.

- Open the user interface:

`nmtui`

- Show a list of available connections, with the option to activate or deactivate them:

`nmtui connect`

- Connect to a given network:

`nmtui connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid|device|SSID</span>

- Edit/Add/Delete a given network:

`nmtui edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|id</span>

- Set the system hostname:

`nmtui hostname`
