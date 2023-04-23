---
layout: page
title: linux/makepkg (polski)
description: "Utwórz pakiet do użycia przez `pacman`-a."
content_hash: 18fe9bbbee698500208a2022cc6afe452cf4da02
last_modified_at: 2023-04-23
related_topics:
  - title: English version
    url: /en/linux/makepkg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># makepkg

Utwórz pakiet do użycia przez `pacman`-a.
Domyślnie używa pliku `PKGBUILD` w aktualnym katalogu roboczym.
Więcej informacji: <https://man.archlinux.org/man/makepkg.8>.

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
