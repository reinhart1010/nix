---
layout: page
title: linux/ego (English)
description: "Funtoo's official system personality management tool."
content_hash: e86698e4688da0d859258326d6d3b7cfba77be0b
---
# ego

Funtoo's official system personality management tool.
More information: <https://funtoo-ego.readthedocs.io/en/develop/>.

- Synchronize the Portage tree:

`ego sync`

- Update the bootloader configuration:

`ego boot update`

- Read a Funtoo wiki page by name:

`ego doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wiki_page</span>

- Print current profile:

`ego profile show`

- Enable/Disable mix-ins:

`ego profile mix-in +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnome</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kde-plasma-5</span>

- Query Funtoo bugs, related to a specified package:

`ego query bug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
