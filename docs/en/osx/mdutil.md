---
layout: page
title: osx/mdutil (English)
description: "Manage the metadata stores used by Spotlight for indexing."
content_hash: e66fda3c6cdd9f87a67b835b28f5249a4f192868
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/osx/mdutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mdutil

Manage the metadata stores used by Spotlight for indexing.
More information: <https://keith.github.io/xcode-man-pages/mdutil.1.html>.

- Show the indexing status of the startup volume:

`mdutil -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- Turn on/off the Spotlight indexing for a given volume:

`mdutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume</span>

- Turn on/off indexing for all volumes:

`mdutil -a -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Erase the metadata stores and restart the indexing process:

`mdutil -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume</span>
