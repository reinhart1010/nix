---
layout: page
title: sunos/svccfg (polski)
description: "Importuj, eksportuj i modyfikuj konfigurację usług."
content_hash: 4f85397798e7359d6da0c94f756c7d1d40bff094
last_modified_at: 2024-05-10
related_topics:
  - title: English version
    url: /en/sunos/svccfg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svccfg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svccfg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svccfg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svccfg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svccfg

Importuj, eksportuj i modyfikuj konfigurację usług.
Więcej informacji: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Sprawdź poprawność pliku konfiguracyjnego:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_smf.xml</span>

- Eksportuj konfigurację usług do pliku:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_usługi</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_smf.xml</span>

- Importuj/aktualizuj konfigurację usług z pliku:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_smf.xml</span>
