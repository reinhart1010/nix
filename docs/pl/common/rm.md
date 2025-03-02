---
layout: page
title: common/rm (polski)
description: "Usuwa pliki lub foldery."
content_hash: 5e7d775baff07aee7bff0ffd368ab33d5e6f9417
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/rm.html
    icon: bi bi-globe
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
  - title: Nederlands version
    url: /nl/common/rm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rm

Usuwa pliki lub foldery.
Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Usuń pliki z dowolnej lokalizacji:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku1 ścieżka/do/pliku2 ...</span>

- Interaktywnie usuń kilka plików z pytaniem o potwierdzenie przed każdym usunięciem:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik(i)</span>

- Usuń pliki w trybie opisowym, pokazując wiadomość o każdym usuniętym pliku:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/folderu/*</span>

- Rekursywnie usuń folder oraz wszystkie jego podfoldery:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/folderu</span>
