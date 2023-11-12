---
layout: page
title: linux/localectl (polski)
description: "Kontroluj ustawienia regionalne i układ klawiatury systemu."
content_hash: f049f95c7b50d97a07eea25a2b1cec1b3b7d4d31
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/localectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# localectl

Kontroluj ustawienia regionalne i układ klawiatury systemu.
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/localectl.html>.

- Wyświetl aktualne ustawienia regionalne systemu i układu klawiatury:

`localectl`

- Wyświetl dostępne ustawienia regionalne:

`localectl list-locales`

- Ustaw zmienną ustawień regionalnych:

`localectl set-locale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LANG</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pl_PL.UTF-8</span>

- Wyświetl dostępne układy klawiatury:

`localectl list-keymaps`

- Ustaw systemowy układ klawiatury dla konsoli i X11:

`localectl set-keymap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pl</span>
