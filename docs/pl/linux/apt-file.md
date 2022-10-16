---
layout: page
title: linux/apt-file (polski)
description: "Wyszukiwanie plików w pakietach apt, łącznie z tymi jeszcze nie zainstalowanymi."
content_hash: cb7f8aced37bb14df2b945d7ecfd33e9277ee092
related_topics:
  - title: català version
    url: /ca/linux/apt-file.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-file.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-file.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
---
# apt-file

Wyszukiwanie plików w pakietach apt, łącznie z tymi jeszcze nie zainstalowanymi.
Więcej informacji: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Aktualizacja bazy metadanych:

`sudo apt update`

- Wyszukanie pakietu, który zawiera określony plik lub ścieżkę:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">część/ścieżki/do/pliku</span>

- Wyświetlenie zawartości określonego pakietu:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyszukanie pakietów, które pasują do podanego `wyrażenia_regularnego`:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` --regexp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wyrażenie_regularne</span>
