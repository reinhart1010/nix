---
layout: page
title: common/xzcmp (Nederlands)
description: "Roep `cmp` aan op bestanden die gecomprimeerd zijn met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`."
content_hash: 7b7dcbe7c2ec11be667a93214ad8c971b0525687
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/xzcmp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xzcmp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xzcmp

Roep `cmp` aan op bestanden die gecomprimeerd zijn met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`.
Alle opgegeven opties worden rechtstreeks doorgegeven aan `cmp`.
Meer informatie: <https://manned.org/xzcmp>.

- Vergelijk twee specifieke bestanden:

`xzcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
