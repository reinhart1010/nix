---
layout: page
title: linux/duc (English)
description: "A collection of tools for indexing, inspecting and visualizing disk usage."
content_hash: ee25f31918aa5e15243cef6064e1cf5101bf5770
last_modified_at: 2024-10-09
related_topics:
  - title: Nederlands version
    url: /nl/linux/duc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duc

A collection of tools for indexing, inspecting and visualizing disk usage.
Duc maintains a database of accumulated sizes of directories in the file system, allowing to query this database, or creating fancy graphs to show where data is.
More information: <http://duc.zevv.nl>.

- Index the `/usr` directory, writing to the default database location `~/.duc.db`:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- List all files and directories under `/usr/local`, showing relative file sizes in a [g]raph:

`duc ls --classify --graph `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- List all files and directories under `/usr/local` using treeview recursively:

`duc ls --classify --graph --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Start the graphical interface to explore the file system using sunburst graphs:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Run the ncurses console interface to explore the file system:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Dump database info:

`duc info`
