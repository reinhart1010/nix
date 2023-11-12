---
layout: page
title: linux/ac (polski)
description: "Wyświetl statystyki dotyczące czasu połączenia użytkowników."
content_hash: dce7f7b23e6a9dc619ecc14a986f8897a69e31e8
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

Wyświetl statystyki dotyczące czasu połączenia użytkowników.
Więcej informacji: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Wyświetl w godzinach jak długo aktualny użytkownik był połączony:

`ac`

- Wyświetl ile godzin użytkownicy byli połączeni:

`ac --individual-totals`

- Wyświetl ile godzin konkretny użytkownik był połączony:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik</span>

- Wyświetl ile godzin na dzień konkretny użytkownik był podłączony (z podsumowaniem):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik</span>

- Wyświetlaj także dodatkowe szczegóły:

`ac --compatibility`
