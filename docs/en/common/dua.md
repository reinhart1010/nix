---
layout: page
title: common/dua (English)
description: "Dua (Disk Usage Analyzer): get the disk space usage of a directory."
content_hash: d84fa33a7edda72d1d9cc81b32889e17b0645e54
last_modified_at: 2024-02-15
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/dua.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dua

Dua (Disk Usage Analyzer): get the disk space usage of a directory.
More information: <https://github.com/Byron/dua-cli>.

- Analyze specific directory:

`dua `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display apparent size instead of disk usage:

`dua --apparent-size`

- Count hard-linked files each time they are seen:

`dua --count-hard-links`

- Aggregate the consumed space of one or more directories or files:

`dua aggregate`

- Launch the terminal user interface:

`dua interactive`

- Format printing byte counts:

`dua --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric|binary|bytes|GB|GiB|MB|MiB</span>

- Use a specific number of threads (defaults to the process number of threads):

`dua --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>
