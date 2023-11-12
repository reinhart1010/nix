---
layout: page
title: linux/apt-key (italiano)
description: "Servizio di gestione delle chiavi per il gestore di pacchetti APT su Debian ed Ubuntu."
content_hash: d63140f658d86b4c5a154b0b1cc148985054b4d8
last_modified_at: 2023-11-12
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
  - title: polski version
    url: /pl/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-key

Servizio di gestione delle chiavi per il gestore di pacchetti APT su Debian ed Ubuntu.
Maggiori informazioni: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Elenca le chiavi fidate:

`apt-key list`

- Aggiunge una chiave al portachiavi delle chiavi fidate:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_chiave_pubblica.asc</span>

- Elimina una chiave dal portachiavi delle chiavi fidate:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_chiave</span>

- Aggiunge una chiave remota al portachiavi delle chiavi fidate:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://indirizzo.tld/filename.key</span>` | apt-key add -`

- Aggiunge una chiave da un server di chiavi con il solo id della chiave:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID_DELLA_CHIAVE</span>
