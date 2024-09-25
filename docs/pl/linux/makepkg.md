---
layout: page
title: linux/makepkg (polski)
description: "Utwórz pakiet do użycia przez `pacman`-a."
content_hash: 34d6a51d41118814a3931e3dd4277d16f9c24ba6
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/makepkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/makepkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/makepkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# makepkg

Utwórz pakiet do użycia przez `pacman`-a.
Domyślnie używa pliku `PKGBUILD` w aktualnym katalogu roboczym.
Więcej informacji: <https://manned.org/makepkg.8>.

- Utwórz pakiet:

`makepkg`

- Utwórz pakiet i zainstaluj jego zależności:

`makepkg --syncdeps`

- Utwórz pakiet, zainstaluj jego zależności, a następnie zainstaluj utworzony pakiet:

`makepkg --syncdeps --install`

- Utwórz pakiet, ale pomiń sprawdzanie sum kontrolnych źrodeł:

`makepkg --skipchecksums`

- Wyczyść katalogi robocze po udanym budowaniu:

`makepkg --clean`

- Zwerifikuj sumy kontrolne źródeł:

`makepkg --verifysource`

- Wygeneruj i zapisz informacje o źródłach do pliku `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`
