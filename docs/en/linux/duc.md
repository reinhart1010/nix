---
layout: page
title: linux/duc (English)
description: "A collection of tools for indexing, inspecting and visualizing disk usage."
content_hash: a682d256b7cf14c1b95ec97bf26a380cdfc0bb93
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# duc

A collection of tools for indexing, inspecting and visualizing disk usage.
Duc maintains a database of accumulated sizes of directories in the file system, allowing to query this database, or creating fancy graphs to show where data is.
More information: <https://duc.zevv.nl/>.

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
