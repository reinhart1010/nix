---
layout: page
title: linux/homectl (polski)
description: "Twórz, usuwaj, zmieniaj lub sprawdzaj katalogi domowe używając usługi systemd-homed."
content_hash: 45b526707dbbcc93895f1570a3f8b6222cf0385c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/homectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# homectl

Twórz, usuwaj, zmieniaj lub sprawdzaj katalogi domowe używając usługi systemd-homed.
Więcej informacji: <https://manned.org/homectl>.

- Wyświetl konta użytkowników i ich powiązane katalogi domowe:

`homectl list`

- Utwórz konto użytkownika i jego powiązany katalog domowy:

`sudo homectl create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Usuń podanego użytkownika i jego powiązany katalog domowy:

`sudo homectl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Zmień hasło podanego użytkownika:

`sudo homectl passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Uruchom powłokę lub komendę z dostępem do podanego katalogu domowego:

`sudo homectl with `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenty_dla_komendy</span>

- Zablokuj lub odblokuj podany katalog domowy:

`sudo homectl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock|unlock</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Zmień miejsce na dysku przydzielone dla podanego katalogu domowego na 100 GiB:

`sudo homectl resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100G</span>

- Wyświetl pomoc:

`homectl --help`
