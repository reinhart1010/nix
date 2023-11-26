---
layout: page
title: common/tldr (polski)
description: "Wyświetl proste strony pomocy dla narzędzi wiersza poleceń z projektu tldr-pages."
content_hash: 90d322b1db47e99150851a7f49742fa5e1dc1df3
last_modified_at: 2023-11-26
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/tldr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/tldr.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tldr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr

Wyświetl proste strony pomocy dla narzędzi wiersza poleceń z projektu tldr-pages.
Uwaga: opcje `--language` i `--list` nie są wymagane przez specyfikację, ale większość klientów je implementuje.
Więcej informacji: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Wyświetl stronę tldr dla podanej komendy (wskazówka: w ten sposób tu trafiłeś/aś!):

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>

- Wyświetl stronę tldr dla podanej podkomendy:

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">podkomenda</span>

- Wyświetl stronę tldr dla komendy w podanym języku (jeżeli jest dostępna, w przeciwnym razie po angielsku):

`tldr --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kod_języka</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>

- Wyświetl stronę tldr dla komendy z podanej platformy:

`tldr --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>

- Zaktualizuj lokalną pamięć podręczną stron tldr:

`tldr --update`

- Wyświetl listę stron tldr dla aktualnej platformy i `common`:

`tldr --list`
