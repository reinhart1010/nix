---
layout: page
title: windows/choco-list (polski)
description: "Wyświetlanie listy pakietów Chocolatey."
content_hash: 8e024ed7bb294615d346dce4512143d75716dd8b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco list

Wyświetlanie listy pakietów Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-list>.

- Wyświetlanie wszystkich dostępnych pakietów:

`choco list`

- Wyświetlanie wszystkich lokalnie zainstalowanych pakietów:

`choco list --local-only`

- Wyświetlanie listy pakietów zawierającej lokalnie zainstalowane programy:

`choco list --include-programs`

- Wyświetlanie listy wyłącznie zatwierdzonych pakietów:

`choco list --approved-only`

- Wyświetlanie listy pakietów dpstępnych w podanym źródle/repozytorium:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url|alias</span>

- PPodanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>
