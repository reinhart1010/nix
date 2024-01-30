---
layout: page
title: linux/shiny-mirrors (English)
description: "Generate a `pacman` mirror list for Manjaro Linux."
content_hash: 475e3de7d58a324259af27a1afb6bce6f7efcfef
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# shiny-mirrors

Generate a `pacman` mirror list for Manjaro Linux.
Every run of shiny-mirrors requires you to synchronize your database and update your system using `sudo pacman -Syyu`.
More information: <https://gitlab.com/Arisa_Snowbell/shiny-mirrors/-/blob/domina/shiny-mirrors/man/shiny-mirrors.md>.

- Get the status of the current mirrors:

`shiny-mirrors status`

- Generate a mirror list using the default behavior:

`sudo shiny-mirrors refresh`

- Display the current configuration file:

`shiny-mirrors config show`

- Switch to a different branch interactively:

`sudo shiny-mirrors config --branch`
