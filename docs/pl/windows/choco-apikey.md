---
layout: page
title: windows/choco-apikey (polski)
description: "Zarządzanie kluczami API dla żródeł Chocolatey."
content_hash: fb75ad5dcb503bde32fb5a0fe9206e90ba000fca
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-apikey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco apikey

Zarządzanie kluczami API dla żródeł Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-apikey>.

- Wyświetlanie listy żródeł wraz z kluczami API:

`choco apikey`

- Wyświetlanie konkrentego źródła wraz z kluczem API:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>`"`

- Ustawienie klucza API dla podanego źródła:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klucz_api</span>`"`

- Usuwanie klucza API dla podanego źródła:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>`" --remove`
