---
layout: page
title: linux/systemd-path (English)
description: "List and query system and user paths."
content_hash: 91678aa3e4d2cffe09db41d5b306f1a02a7b521c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-path

List and query system and user paths.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-path.html>.

- Display a list of known paths and their current values:

`systemd-path`

- Query the specified path and display its value:

`systemd-path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path_name</span>`"`

- Suffix printed paths with `suffix_string`:

`systemd-path --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suffix_string</span>

- Print a short version string and then exit:

`systemd-path --version`
