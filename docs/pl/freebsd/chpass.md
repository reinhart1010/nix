---
layout: page
title: freebsd/chpass (polski)
description: "Dodaj lub zmień informacje w bazie danych użytkowników, w tym powłokę logowania i hasło."
content_hash: e395c2f5698e4dbc04c9e8ecd77fe82d2072f9b0
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/freebsd/chpass.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/freebsd/chpass.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/chpass.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

Dodaj lub zmień informacje w bazie danych użytkowników, w tym powłokę logowania i hasło.
Zobacz także: `passwd`.
Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Dodaj lub zmień informacje w bazie danych użytkowników dla bieżącego użytkownika w sposób interaktywny:

`su -c chpass`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla bieżącego użytkownika:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>

- Ustaw powłokę (z ang. [s]hell) logowania dla określonego użytkownika:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Zmień czas wygaśnięcia (z ang. [e]xpire) konta (w sekundach od daty początku epoki, UTC):

`su -c 'chpass -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">czas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>`'`

- Zmień hasło użytkownika:

`su -c 'chpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zaszyfrowane_hasło</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>`'`

- Określ nazwę [h]osta lub adres serwera NIS do zapytania:

`su -c 'chpass -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_hosta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>`'`

- Określ konkretną [d]omenę NIS (domyślnie nazwa domeny systemowej):

`su -c 'chpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>`'`
