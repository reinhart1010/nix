---
layout: page
title: sunos/truss (polski)
description: "Narzędzie do rozwiązywania problemów poprzez śledzenie wywołań systemowych."
content_hash: 070b807ea6de9d494abe4655cc842a0803a7bbab
last_modified_at: 2024-09-04
related_topics:
  - title: English version
    url: /en/sunos/truss.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/truss.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/sunos/truss.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/truss.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/truss.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/truss.html
    icon: bi bi-globe
tldri18n_status: 2
---
# truss

Narzędzie do rozwiązywania problemów poprzez śledzenie wywołań systemowych.
Odpowiednik strace w SunOS.
Więcej informacji: <https://www.unix.com/man-page/linux/1/truss>.

- Rozpocznij śledzenie programu, wykonując go i śledząc wszystkie procesy potomne:

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Rozpocznij śledzenie określonego procesu według jego PID:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Rozpocznij śledzenie programu, wykonując go, pokazując argumenty i zmienne środowiskowe:

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Zlicz czas, wywołania i błędy dla każdego wywołania systemowego i raportuj podsumowanie po zakończeniu programu:

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Śledź proces filtrując dane wyjściowe według wywołania systemowego:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_wywołania_systemowego</span>
