---
layout: page
title: linux/protontricks (English)
description: "A simple wrapper that does Winetricks things for Proton enabled games, requires Winetricks."
content_hash: 2bf3268d5b2086b1c551d3f574d2fae8d515ec4e
---
# protontricks

A simple wrapper that does Winetricks things for Proton enabled games, requires Winetricks.
More information: <https://github.com/Matoking/protontricks>.

- Show the protontricks help message:

`protontricks`

- Run the protontricks GUI:

`protontricks --gui`

- Run Winetricks for a specific game:

`protontricks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">winetricks_args</span>

- Run a command within a game's installation directory:

`protontricks -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>
