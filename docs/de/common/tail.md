---
layout: page
title: common/tail (Deutsch)
description: "Gib das Ende einer Datei aus."
content_hash: a6709de0aea887652517e81b88167040beef6759
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tail.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tail.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tail.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tail.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tail.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tail

Gib das Ende einer Datei aus.
Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Zeige die letzten Zeilen einer Datei an:

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_zeilen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Zeige alle Zeilen einer Datei ab einer bestimmten Zeile an:

`tail --lines +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zeile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Zeige die letzten Bytes einer Datei an:

`tail --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird:

`tail --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird, selbst, wenn die Datei nicht zugänglich ist:

`tail --retry --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>

- Zeige die letzten Zeilen einer Datei an und lade alle paar Sekunden neu:

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_zeilen</span>` --sleep-interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_sekunden</span>` --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>
