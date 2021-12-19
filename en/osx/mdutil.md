---
layout: page
title: osx/mdutil (English)
description: "Manage the metadata stores used by Spotlight for indexing."
content_hash: e90d2a436b7bf61122310a456d30be66f8b64218
related_topics:
  - title: 中文 version
    url: /zh/osx/mdutil.html
    icon: bi bi-globe
---
# mdutil

Manage the metadata stores used by Spotlight for indexing.
More information: <https://ss64.com/osx/mdutil.html>.

- Show the indexing status of the startup volume:

`mdutil -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- Turn on/off the Spotlight indexing for a given volume:

`mdutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume</span>

- Turn on/off indexing for all volumes:

`mdutil -a -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Erase the metadata stores and restart the indexing process:

`mdutil -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume</span>
