---
layout: page
title: linux/apt-key (polski)
description: "Narzędzie do zarządzania kluczami menedżera pakietów APT dla Debiana i Ubuntu."
content_hash: 047eae4c02a93b58f6b30e405abbcb1bfe998042
last_modified_at: 2024-09-18
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
  - title: українська version
    url: /uk/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-key

Narzędzie do zarządzania kluczami menedżera pakietów APT dla Debiana i Ubuntu.
Notatka: `apt-key` jest aktualnie przestarzały (za wyjątkiem użycia `apt-key del` w skryptach opiekunów).
Więcej informacji: <https://manned.org/apt-key.8>.

- Wyświetl zaufane klucze:

`apt-key list`

- Dodaj klucz do magazynu zaufanych kluczy:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_z_kluczem_publicznym.asc</span>

- Usuń klucz z magazynu zaufanych kluczy:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_klucza</span>

- Dodaj zdalny klucz do magazynu zaufanych kluczy:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/nazwa_pliku.key</span>` | apt-key add -`

- Dodaj klucz z serwera kluczy na podstawie ID klucza:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_klucza</span>
