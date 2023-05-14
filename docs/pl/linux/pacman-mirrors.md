---
layout: page
title: linux/pacman-mirrors (polski)
description: "Wygeneruj listę serwerów lustrzanych dla Manjaro Linuksa."
content_hash: 56e98ee63c57422e11aa4476ff275f2d1edac6ff
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-mirrors.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman-mirrors

Wygeneruj listę serwerów lustrzanych dla Manjaro Linuksa.
Każde uruchomienie pacman-mirrors wymaga zsynchronizowanej bazy danych oraz zaktualizowania systemu używając `sudo pacman -Syyu`.
Zobacz także: `pacman`.
Więcej informacji: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Wygeneruj listę serwerów lustrzanych używając domyślnych ustawień:

`sudo pacman-mirrors --fasttrack`

- Wyświetl status aktualnych serwerów lustrzanych:

`pacman-mirrors --status`

- Pokaż aktualną gałąź:

`pacman-mirrors --get-branch`

- Przęłącz na inną gałąź:

`sudo pacman-mirrors --api --set-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|unstable|testing</span>

- Wygeneruj listę serwerów lustrzanych, używając tylko tych w twoim kraju:

`sudo pacman-mirrors --geoip`
