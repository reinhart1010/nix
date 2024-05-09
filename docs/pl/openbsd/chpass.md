---
layout: page
title: openbsd/chpass (polski)
description: "Dodaj lub zmień informacje o użytkowniku w bazie danych, w tym powłoki logowania i hasła."
content_hash: 02fb7925a558c63c440c1ab4e0d33534d167739f
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

Dodaj lub zmień informacje o użytkowniku w bazie danych, w tym powłoki logowania i hasła.
Zobacz także: `passwd`.
Więcej informacji: <https://man.openbsd.org/chsh>.

- Interaktywnie ustaw określoną powłokę logowania dla bieżącego użytkownika:

`doas chsh`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla bieżącego użytkownika:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla określonego użytkownika:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/powłoki</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Określ wpis bazy danych użytkownika w formacie pliku `passwd`:

`doas chsh -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika:zaszyfrowane_hasło:uid:gid:...</span>
