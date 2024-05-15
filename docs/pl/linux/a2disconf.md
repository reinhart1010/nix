---
layout: page
title: linux/a2disconf (polski)
description: "Wyłącz plik konfiguracyjny Apache w systemach opartych na Debianie."
content_hash: a1cba871a5713395e2eed54be385f5006d382798
last_modified_at: 2024-05-15
related_topics:
  - title: català version
    url: /ca/linux/a2disconf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2disconf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2disconf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/a2disconf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2disconf.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2disconf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2disconf.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2disconf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/a2disconf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2disconf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/a2disconf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># a2disconf

Wyłącz plik konfiguracyjny Apache w systemach opartych na Debianie.
Więcej informacji: <https://manpages.debian.org/latest/apache2/a2disconf.8.en.html>.

- Wyłącz plik konfiguracyjny:

`sudo a2disconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_konfiguracyjny</span>

- Nie pokazuj wiadomości informacyjnych:

`sudo a2disconf --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_konfiguracyjny</span>
