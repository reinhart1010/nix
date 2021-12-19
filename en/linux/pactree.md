---
layout: page
title: linux/pactree (English)
description: "Package dependency tree viewer for pacman."
content_hash: ff572b853933a2db63158042c2795af7930a99c2
---
# pactree

Package dependency tree viewer for pacman.
More information: <https://man.archlinux.org/man/pactree.8>.

- Print the dependency tree of a specific package:

`pactree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Print what packages depend on a specific package:

`pactree --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Dump dependencies one per line, skipping duplicates:

`pactree --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Include optional dependencies of a specific package and colorize the output:

`pactree --optional --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display help:

`pactree`
