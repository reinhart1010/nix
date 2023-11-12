---
layout: page
title: common/clear (Deutsch)
description: "Leert den Bildschirm eines Terminals."
content_hash: 7977735a6a0a8a44467e4c2fd9bd70bc8cf1f4b5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/clear.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/clear.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clear

Leert den Bildschirm eines Terminals.
Weitere Informationen: <https://manned.org/clear>.

- Leere den Bildschirm (äquivalent zu Strg+L in einer Bash Shell):

`clear`

- Leere den Bildschirm, aber erhalte den Rückscroll-Puffer des Terminals:

`clear -x`

- Lege den Typ des zu leerenden Terminals fest (Standardwert ist die Umgebungsvariable $TERM):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">typ_des_terminals</span>

- Zeige die Version von `ncurses` an, die von `clear` benutzt wird:

`clear -V`
