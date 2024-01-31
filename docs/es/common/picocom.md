---
layout: page
title: common/picocom (español)
description: "Programa minimalista para emular consolas serie."
content_hash: bcd2a8c3b56b3484cc882e78a46b93c0faa18ea6
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/common/picocom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/picocom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># picocom

Programa minimalista para emular consolas serie.
Más información: <https://manned.org/picocom>.

- Conecta a una consola serie con una velocidad en baudios específica:

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baud_rate</span>

- Asigna caracteres especiales (por ejemplo, `LF` a `CRLF`):

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf}</span>
