---
layout: page
title: linux/apx-pkgmanagers (English)
description: "Manage package managers in `apx`."
content_hash: 9361b7a75ffbb102a8a63251b719efb2f4327ab8
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/linux/apx-pkgmanagers.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx pkgmanagers

Manage package managers in `apx`.
Note: user-created package manager configurations are stored in `~/.local/share/apx/pkgmanagers`.
More information: <https://github.com/Vanilla-OS/apx>.

- Interactively create a new package manager configuration:

`apx pkgmanagers create`

- List all available package manager confirgurations:

`apx pkgmanagers list`

- Remove a package manager configuration:

`apx pkgmanagers rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Display information about a specific package manager:

`apx pkgmanagers show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
