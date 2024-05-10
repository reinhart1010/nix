---
layout: page
title: sunos/devfsadm (polski)
description: "Komenda administracyjna dla `/dev`. Zarządza przestrzenią nazw `/dev`."
content_hash: d9a70ff98b9915771cb670785df5c9027fb2a680
last_modified_at: 2024-05-10
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

Komenda administracyjna dla `/dev`. Zarządza przestrzenią nazw `/dev`.
Więcej informacji: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Skanuj w poszukiwaniu nowych dysków:

`devfsadm -c disk`

- Wyczyść wszystkie wiszące linki /dev i skanuj w poszukiwaniu nowego urządzenia:

`devfsadm -C -v`

- Próbne uruchomienie - wypisz to, co zostanie zmienione, ale bez wprowadzania modyfikacji:

`devfsadm -C -v -n`
