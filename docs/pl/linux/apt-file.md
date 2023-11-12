---
layout: page
title: linux/apt-file (polski)
description: "Wyszukaj pliki w pakietach apt, w tym jeszcze nie zainstalowanych."
content_hash: 048d8cf55a949f95e7e3c09c73838eab6590bd12
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# apt-file

Wyszukaj pliki w pakietach apt, w tym jeszcze nie zainstalowanych.
Więcej informacji: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Zaktualizuj bazę metadanych:

`sudo apt update`

- Wyszukaj pakiet, który zawiera określony plik lub ścieżkę:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">część/ścieżki/do/pliku</span>

- Wyświetl zawartośċ określonego pakietu:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyszukaj pakiety, które pasują do podanego `wyrażenia_regularnego`:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` --regexp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wyrażenie_regularne</span>
