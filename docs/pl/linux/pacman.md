---
layout: page
title: linux/pacman (polski)
description: "Narzędzie do zarządzania pakietami w Arch Linuksie."
content_hash: 96220e9d75a10ae0e639c5f1fa6b96013d3ccf55
last_modified_at: 2024-01-02
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Narzędzie do zarządzania pakietami w Arch Linuksie.
Zobacz także: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
Odpowiednie polecenia dla innych menedżerów pakietów: <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Zsynchronizuj i zaktualizuj wszystkie pakiety:

`sudo pacman -Syu`

- Zainstaluj nowy pakiet:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usuń pakiet i jego zależności:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Poszukaj w bazie danych pakietów zawierających podany plik:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pliku</span>`"`

- Wyświetl zainstalowane pakiety i ich wersje:

`pacman -Q`

- Wyświetl tylko pakiety niebędące zależnościami i ich wersje:

`pacman -Qe`

- Wyświetl pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`pacman -Qtdq`

- Wyczyść całą pamięć podręczną pacmana:

`sudo pacman -Scc`
