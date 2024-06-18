---
layout: page
title: common/picocom (español)
description: "Programa minimalista para emular consolas serie."
content_hash: 1fcea5a8331393f6ff7bc0ecdffa8ec91d217527
last_modified_at: 2024-06-18
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

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tasa_de_baudios</span>

- Asigna caracteres especiales (p. ej. `LF` a `CRLF`):

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf</span>
