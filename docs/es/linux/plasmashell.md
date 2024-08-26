---
layout: page
title: linux/plasmashell (español)
description: "Inicia y reinicia Plasma Desktop."
content_hash: abca4787b563ac0acbe48f526df4ae57b09dad69
last_modified_at: 2024-08-26
related_topics:
  - title: English version
    url: /en/linux/plasmashell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# plasmashell

Inicia y reinicia Plasma Desktop.
Más información: <https://invent.kde.org/plasma/plasma-desktop>.

- Reinicia `plasmashell`:

`systemctl restart --user plasma-plasmashell`

- Reinicia `plasmashell` sin systemd:

`plasmashell --replace & disown`

- Muestra ayuda en las opciones de la línea de comandos:

`plasmashell --help`

- Muestra la ayuda, incluidas las opciones de Qt:

`plasmashell --help-all`
