---
layout: page
title: common/yes (polski)
description: "Wypisuje coś wielokrotnie."
content_hash: f6d08f74cf7f88b6e92efc4838ace13cc0c57406
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yes.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/yes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/yes.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yes

Wypisuje coś wielokrotnie.
Komenda używana często aby potwierdzić pytania zadawane przez komendy instalujące takie jak apt-get.
Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- Wypisuj bez końca "wiadomość":

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wiadomość</span>

- Wypisuj bez końca "y":

`yes`

- Wysyłaj potwierdzenie dla każdego pytania zadanego przez `apt-get`:

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Wielokrotnie wypisuj znak nowej linii, aby zawsze akceptować domyślne opcje poleceń:

`yes ''`
