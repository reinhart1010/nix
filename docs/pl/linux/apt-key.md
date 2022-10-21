---
layout: page
title: linux/apt-key (polski)
description: "Narzędzie do zarządzania kluczami APT Package Manager dla Debiana i Ubuntu."
content_hash: 7d3669f59007e7a2004c674e32f8acad9ebc3104
related_topics:
  - title: català version
    url: /ca/linux/apt-key.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-key.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-key.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-key.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
---
# apt-key

Narzędzie do zarządzania kluczami APT Package Manager dla Debiana i Ubuntu.
Notatka: `apt-key` jest aktualnie przestarzały (za wyjątkiem użycia `apt-key del` w skryptach opiekunów).
Więcej informacji: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Wyświetl zaufane klucze:

`apt-key list`

- Dodanie klucza do magazynu zaufanych kluczy:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_z_kluczem_publicznym.asc</span>

- Usunięcie klucza z magazynu zaufanych kluczy:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_klucza</span>

- Dodanie zdalnego klucza do magazynu zaufanych kluczy:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/nazwa_pliku.key</span>` | apt-key add -`

- Dodanie klucza z serwera kluczy na podstawie id klucza:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_klucza</span>
