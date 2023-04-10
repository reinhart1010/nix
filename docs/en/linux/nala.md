---
layout: page
title: linux/nala (English)
description: "Package management Utility."
content_hash: 8f52744ce2be37230fd550f628cf15a64bee41a7
last_modified_at: 2023-04-10
---
# nala

Package management Utility.
Wrapper for the `apt` package manager.
More information: <https://gitlab.com/volian/nala>.

- Install a package, or update it to the latest available version:

`nala install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`sudo nala remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its configuration files:

`nala purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search package names and descriptions using a word, regex (default) or glob:

`sudo nala search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`

- Update the list of available packages and upgrade the system:

`nala upgrade`

- Remove all unused packages and dependencies from your system:

`nala autoremove`

- Fetch fast mirrors to improve download speeds:

`nala fetch`

- Display the history of all transactions:

`nala history`
