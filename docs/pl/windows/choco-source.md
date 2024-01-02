---
layout: page
title: windows/choco-source (polski)
description: "Zarządzaj źródłami/repozytoriami pakietów Chocolatey."
content_hash: ca3a11402a7b984386c8d6f58bebed495ca6a91e
last_modified_at: 2024-01-02
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-source.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-source.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-source.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-source.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-source.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-source.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco source

Zarządzaj źródłami/repozytoriami pakietów Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-source>.

- Wyświetl aktualnie dostępne źródła:

`choco source list`

- Dodaj nowe źródło:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>

- Dodaj nowe źródło z użyciem poświadczeń:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>

- Dodaj nowe źródło z użyciem certyfikatu:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>` --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/certyfikatu</span>

- Włącz dane źródło/repozytorium pakietów:

`choco source enable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>

- Wyłącz dane źródło/repozytorium pakietów:

`choco source disable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>

- Usuń dane źródło/repozytorium:

`choco source remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>
