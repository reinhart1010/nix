---
layout: page
title: linux/nala (English)
description: "Package management utility with better formatting."
content_hash: 0922b952507a5182cdcdd7b42bb559d0b8e71acf
last_modified_at: 2024-01-09
tldri18n_status: 2
---
# nala

Package management utility with better formatting.
Front-end for the `python-apt` API.
More information: <https://gitlab.com/volian/nala>.

- Install a package, or update it to the latest available version:

`sudo nala install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`sudo nala remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its configuration files:

`nala purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search package names and descriptions using a word, regex (default) or glob:

`nala search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`

- Update the list of available packages and upgrade the system:

`sudo nala upgrade`

- Remove all unused packages and dependencies from your system:

`sudo nala autoremove`

- Fetch fast mirrors to improve download speeds:

`sudo nala fetch`

- Display the history of all transactions:

`nala history`
