---
layout: page
title: common/yes (polski)
description: "Wypisuje coś wielokrotnie."
content_hash: 24f462af5fc48b485cef38e43a5e2b61290050f8
last_modified_at: 2024-06-14
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
  - title: Nederlands version
    url: /nl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/yes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yes

Wypisuje coś wielokrotnie.
Komenda używana często aby potwierdzić pytania zadawane przez komendy instalujące takie jak apt-get.
Więcej informacji: <https://www.gnu.org/software/coreutils/yes>.

- Wypisuj bez końca "wiadomość":

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wiadomość</span>

- Wypisuj bez końca "y":

`yes`

- Wysyłaj potwierdzenie dla każdego pytania zadanego przez `apt-get`:

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Wielokrotnie wypisuj znak nowej linii, aby zawsze akceptować domyślne opcje poleceń:

`yes ''`
