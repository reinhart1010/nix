---
layout: page
title: linux/protontricks (English)
description: "A simple wrapper that runs Winetricks commands for Proton enabled games."
content_hash: 65172c41a9ae036ae0b15e24e92c1e56d72b5861
last_modified_at: 2024-12-08
related_topics:
  - title: 한국어 version
    url: /ko/linux/protontricks.html
    icon: bi bi-globe
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

- Run an executable in the proton environment of a specific game:

`protontricks-launch --appid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable.exe</span>

- Display help:

`protontricks --help`
