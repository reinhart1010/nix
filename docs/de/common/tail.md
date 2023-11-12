---
layout: page
title: common/tail (Deutsch)
description: "Gib das Ende einer Datei aus."
content_hash: 642dd0fef6ba16e1254c2c8ba064b00069e52287
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tail.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tail.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tail

Gib das Ende einer Datei aus.
Weitere Informationen: <https://www.gnu.org/software/coreutils/tail>.

- Zeige die letzten Zeilen einer Datei an:

`tail -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_zeilen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Zeige alle Zeilen einer Datei ab einer bestimmten Zeile an:

`tail -n +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zeile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Zeige die letzten Bytes einer Datei an:

`tail -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird:

`tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird, selbst, wenn die Datei nicht zugänglich ist:

`tail -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Zeige die letzten Zeilen einer Datei an und lade alle paar Sekunden neu:

`tail -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_zeilen</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_sekunden</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>
