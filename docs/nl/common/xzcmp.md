---
layout: page
title: common/xzcmp (Nederlands)
description: "Roep `cmp` aan op bestanden die gecomprimeerd zijn met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`."
content_hash: 7b7dcbe7c2ec11be667a93214ad8c971b0525687
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/common/xzcmp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xzcmp

Roep `cmp` aan op bestanden die gecomprimeerd zijn met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`.
Alle opgegeven opties worden rechtstreeks doorgegeven aan `cmp`.
Meer informatie: <https://manned.org/xzcmp>.

- Vergelijk twee specifieke bestanden:

`xzcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
