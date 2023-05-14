---
layout: page
title: linux/pacman (polski)
description: "Narzędzie do zarządzania pakietami w Arch Linuksie."
content_hash: 22dd599c875abb4efaa355bc02207a94ad3ab27e
last_modified_at: 2023-05-14
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
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman

Narzędzie do zarządzania pakietami w Arch Linuksie.
Zobacz także: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
Odpowiednie polecenia dla innych menedżerów pakietów: <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Zsynchronizuj i zaktualizuj wszystkie pakiety:

`sudo pacman -Syu`

- Zainstaluj nowy pakiet:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Usuń pakiet i jego zależności:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Przeszukaj bazę danych pakietów używając wyrażenia regularnego lub słowa klucz:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zapytanie</span>`"`

- Wyświetl zainstalowane pakiety i ich wersje:

`pacman -Q`

- Wyświetl tylko pakiety niebędące zależnościami i ich wersje:

`pacman -Qe`

- Wyświetl pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`pacman -Qtdq`

- Wyczyść całą pamięć podręczną pacmana:

`sudo pacman -Scc`
