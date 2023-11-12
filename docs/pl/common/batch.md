---
layout: page
title: common/batch (polski)
description: "Wykonaj polecenia, gdy pozwoli na to poziom obciążenia systmu."
content_hash: f5518094b9a94069dad9665288f51ff507c0cdee
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# batch

Wykonaj polecenia, gdy pozwoli na to poziom obciążenia systmu.
Aby działać poprawnie wymaga działającego serwisu atd (lub atrun).
Więcej informacji: <https://manned.org/batch>.

- Wykonaj polecenie wprowadzone przy użyciu wejścia standardowego (aby zakończyć naciśnij `Ctrl + D`):

`batch`

- Wykonaj polecenie podane z wejścia standardowego:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./zrób_backup.sh</span>`" | batch`

- Wykonaj polecenia z podanego pliku:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>
