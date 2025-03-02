---
layout: page
title: linux/lookandfeeltool (español)
description: "Cambia los temas globales de Plasma."
content_hash: e1db2479fdc1b47140cd165ff953a84d2232af99
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/lookandfeeltool.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/lookandfeeltool.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lookandfeeltool

Cambia los temas globales de Plasma.
Más información: <https://userbase.kde.org/System_Settings/Look_And_Feel>.

- Lista los temas globales disponibles:

`lookandfeeltool --list`

- Aplica un tema global:

`lookandfeeltool --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.theme.desktop</span>

- Utiliza `lookandfeeltool` sin un servidor de muestra:

`lookandfeeltool --platform offscreen`

- Muestra la ayuda:

`lookandfeeltool --help`
