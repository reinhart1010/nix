---
layout: page
title: sunos/truss (polski)
description: "Narzędzie do rozwiązywania problemów poprzez śledzenie wywołań systemowych."
content_hash: b2b3b382d74ea4ae3c1092ff7833ffaacd1d6706
last_modified_at: 2024-05-09
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
  - title: Nederlands version
    url: /nl/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/truss.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/truss.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># truss

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

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_wywolania_systemowego</span>
