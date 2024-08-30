---
layout: page
title: linux/mac2unix (English)
description: "Change macOS-style line endings to Unix-style."
content_hash: 9ee73163a593191505f544a2481a48c83e777b98
last_modified_at: 2024-08-30
related_topics:
  - title: 中文 version
    url: /zh/linux/mac2unix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mac2unix

Change macOS-style line endings to Unix-style.
Replaces CR with LF.
See also `unix2dos`, `unix2mac`, and `dos2unix`.
More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a copy with Unix-style line endings:

`mac2unix -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_file</span>

- Display file information:

`mac2unix -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Keep/add/remove Byte Order Mark:

`mac2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
