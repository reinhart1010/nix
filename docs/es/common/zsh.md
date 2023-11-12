---
layout: page
title: common/zsh (español)
description: "Z SHell, un intérprete para la línea de comandos compatible con Bash."
content_hash: 47685ab416aae1993e3d9000bd2fc6c793993066
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zsh

Z SHell, un intérprete para la línea de comandos compatible con Bash.
Véase también `histexpand` para la expansión del historial.
Más información: <https://www.zsh.org>.

- Comienza una sesión interactiva en la shell:

`zsh`

- Ejecuta un comando y sale:

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Ejecuta un script:

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.zsh</span>

- Ejecuta un script, mostrando cada comando antes de ejecutarlo:

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.zsh</span>

- Comienza una sesión interactiva en la shell en modo detallado, mostrando cada comando antes de ejecutarlo:

`zsh --verbose`
