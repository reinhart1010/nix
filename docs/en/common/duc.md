---
layout: page
title: common/duc (English)
description: "A collection of tools for indexing, inspecting, and visualizing disk usage."
content_hash: abfab7fc166280eb69be58fe5d9833a50377efff
last_modified_at: 2024-08-13
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/duc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duc

A collection of tools for indexing, inspecting, and visualizing disk usage.
Duc maintains a database of accumulated sizes of directories of the file system, allowing queries in this database, or creating fancy graphs to show where data is.
More information: <https://duc.zevv.nl/>.

- Index the /usr directory, writing to the default database location ~/.duc.db:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- List all files and directories under /usr/local, showing relative file sizes in a [g]raph:

`duc ls -Fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- List all files and directories under /usr/local using treeview recursively:

`duc ls -Fg -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Start the graphical interface to explore the file system using sunburst graphs:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Run the ncurses console interface to explore the file system:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Dump database info:

`duc info`
