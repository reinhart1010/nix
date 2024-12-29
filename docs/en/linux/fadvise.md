---
layout: page
title: linux/fadvise (English)
description: "Control Linux file caching behavior."
content_hash: 292c9b018dcd1b8d88b8c46b9628268cc2c29132
last_modified_at: 2024-12-29
tldri18n_status: 2
---
# fadvise

Control Linux file caching behavior.
More information: <https://manned.org/fadvise>.

- Preload a file into cache:

`fadvise `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--advice</span>` willneed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Suggest dropping a file from cache:

`fadvise `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`fadvise --help`
