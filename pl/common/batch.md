---
layout: page
title: common/batch (polski)
description: "Wykonaj polecenia, gdy pozwoli na to poziom obciążenia systmu."
content_hash: 5acb6637a06e55c1b15fc345bc84701f2de94c61
related_topics:
  - title: English version
    url: /en/common/batch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
---
# batch

Wykonaj polecenia, gdy pozwoli na to poziom obciążenia systmu.
Aby działać poprawnie wymaga działającego serwisu atd (lub atrun).
Więcej informacji: <https://man.archlinux.org/man/at.1>.

- Wykonaj polecenie wprowadzone przy użyciu wejścia standardowego (aby zakończyć naciśnij `Ctrl + D`):

`batch`

- Wykonaj polecenie podane z wejścia standardowego:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./zrób_backup.sh</span>`" | batch`

- Wykonaj polecenia z podanego pliku:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>
