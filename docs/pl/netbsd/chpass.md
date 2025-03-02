---
layout: page
title: netbsd/chpass (polski)
description: "Dodaj lub zmień informacje w bazie danych użytkowników, w tym powłokę logowania i hasło."
content_hash: 4e846ceee6c060e82006129cc5c85e29a73dfdb8
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/netbsd/chpass.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/netbsd/chpass.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

Dodaj lub zmień informacje w bazie danych użytkowników, w tym powłokę logowania i hasło.
Zobacz także: `passwd`.
Więcej informacji: <https://man.netbsd.org/chsh>.

- Ustaw określoną powłokę logowania dla bieżącego użytkownika w sposób interaktywny:

`su -c chpass`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla bieżącego użytkownika:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>

- Ustaw powłokę (z ang. [s]hell) logowania dla określonego użytkownika:

`chpass chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Określ wpis bazy danych użytkownika w formacie pliku `passwd`:

`su -c 'chpass -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika:zaszyfrowane_hasło:uid:gid:...</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Aktualizuj tylko [l]okalny plik haseł:

`su -c 'chpass -l -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Wymuś zmianę wpisu w bazie danych [y]P haseł:

`su -c 'chpass -y -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>
