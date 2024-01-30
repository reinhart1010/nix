---
layout: page
title: linux/protontricks (English)
description: "A simple wrapper that runs Winetricks commands for Proton enabled games."
content_hash: 932cdcada5c0ca236793adcb2b88ea884b9fff56
last_modified_at: 2024-01-30
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/protontricks.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/protontricks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protontricks

A simple wrapper that runs Winetricks commands for Proton enabled games.
More information: <https://github.com/Matoking/protontricks>.

- Run the protontricks GUI:

`protontricks --gui`

- Run Winetricks for a specific game:

`protontricks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">winetricks_args</span>

- Run a command within a game's installation directory:

`protontricks -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>

- [l]ist all installed games:

`protontricks -l`

- [s]earch for a game's App ID by name:

`protontricks -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">game_name</span>

- Display help:

`protontricks --help`
