---
layout: page
title: linux/duc (English)
description: "Duc is a collection of tools for indexing, inspecting and visualizing disk usage. Duc maintains a database of accumulated sizes of directories of the file system, allowing queries this database, or create fancy graphs to show where data is."
content_hash: 678702f3c19440bd762bb176551a401f17c679cd
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># duc

Duc is a collection of tools for indexing, inspecting and visualizing disk usage. Duc maintains a database of accumulated sizes of directories of the file system, allowing queries this database, or create fancy graphs to show where data is.
More information: <https://duc.zevv.nl/>.

- Index the /usr directory, writing to the default database location ~/.duc.db:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- List all files and directories under /usr/local, showing relative file sizes in a [g]raph:

`duc ls --classify --graph `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- List all files and directories under /usr/local using treeview recursively:

`duc ls --classify --graph --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Start the graphical interface to explore the file system using sunburst graphs:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Run the ncurses console interface to explore the file system:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Dump database info:

`duc info`
