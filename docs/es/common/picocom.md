---
layout: page
title: common/picocom (español)
description: "Programa minimalista para emular consolas serie."
content_hash: bcd2a8c3b56b3484cc882e78a46b93c0faa18ea6
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/picocom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# picocom

Programa minimalista para emular consolas serie.
Más información: <https://manned.org/picocom>.

- Conecta a una consola serie con una velocidad en baudios específica:

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baud_rate</span>

- Asigna caracteres especiales (por ejemplo, `LF` a `CRLF`):

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf}</span>
