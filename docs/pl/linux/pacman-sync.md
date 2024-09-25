---
layout: page
title: linux/pacman-sync (polski)
description: "Narzędzie do zarządzania pakietami w Arch Linuksie."
content_hash: 1379b960bcca3e7bd78a6ab9c296306b58c1ffda
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-sync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-sync.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --sync

Narzędzie do zarządzania pakietami w Arch Linuksie.
Zobacz także: `pacman`.
Więcej informacji: <https://manned.org/pacman.8>.

- Zainstaluj nowy pakiet:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Zsynchronizuj i zaktualizuj wszystkie pakiety (użyj `--downloadonly` aby pobrać pakiety i ich nie zaktualizować):

`sudo pacman --sync --refresh --sysupgrade`

- Zaktualizuj wszystkie pakiety i zainstaluj nowy bez pytania:

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Przeszukaj bazę danych pakietów używając wyrażenia regularnego lub słowa klucz:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zapytanie</span>`"`

- Wyświetl informacje o pakiecie:

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Nadpisz pliki będące w konflikcie podczas aktualizacji pakietów:

`sudo pacman --sync --refresh --sysupgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Zsynchronizuj i zaktualizuj wszystkie pakiety, ale zignoruj konkretny pakiet (można użyć więcej niż raz):

`sudo pacman --sync --refresh --sysupgrade --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Usuń niezainstalowane pakiety i nieużywane repozytoria z pamięci podręcznej (użyj dwa razy opcji `--clean`, aby wyczyścić wszystkie pakiety):

`sudo pacman --sync --clean`
