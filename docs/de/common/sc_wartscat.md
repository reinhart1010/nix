---
layout: page
title: common/sc_wartscat (Deutsch)
description: "Füge mehrere `warts`-Dateien zusammen."
content_hash: 0d6b81ce849198d0aa4216db144f6826ebac239e
last_modified_at: 2024-03-20
related_topics:
  - title: English version
    url: /en/common/sc_wartscat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sc_wartscat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc_wartscat

Füge mehrere `warts`-Dateien zusammen.
Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Verkette mehrere `warts`-Dateien zu Einer:

`sc_wartscat -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts path/to/file2.warts ...</span>
