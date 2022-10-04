---
layout: page
title: linux/dconf (English)
description: "Manage dconf databases."
content_hash: 2cea7f63fe66c688c30962063ac113e8d771715f
---
# dconf

Manage dconf databases.
See also: `dconf-read`, `dconf-reset`, `dconf-write`, `gsettings`.
More information: <https://manned.org/dconf>.

- Print a specific key value:

`dconf read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/key</span>

- Print a specific path sub-directories and sub-keys:

`dconf list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/directory/</span>

- Write a specific key value:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/key</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Reset a specific key value:

`dconf reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/key</span>

- Watch a specific key/directory for changes:

`dconf watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/key|/path/to/directory/</span>

- Dump a specific directory in INI file format:

`dconf dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/directory/</span>
