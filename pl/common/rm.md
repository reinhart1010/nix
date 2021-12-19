---
layout: page
title: common/rm (polski)
description: "Usuwa pliki lub foldery."
content_hash: 419d3f88dfaddfa3217030c9bbf3194b75a6d445
related_topics:
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
---
# rm

Usuwa pliki lub foldery.
Więcej informacji: <https://www.gnu.org/software/coreutils/rm>.

- Usuń pliki z dowolnej lokalizacji:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/innego/pliku</span>

- Rekursywnie usuń folder oraz wszystkie jego podfoldery:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/folderu</span>

- Wymuś usunięcie folderu, bez pytania o potwierdzenie lub pokazywania błędów:

`rm -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/folderu</span>

- Interaktywnie usuń kilka plików z pytaniem o potwierdzenie przed każdym usunięciem:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik(i)</span>

- Usuń pliki w trybie opisowym, pokazując wiadomość o każdym usuniętym pliku:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/folderu/*</span>
