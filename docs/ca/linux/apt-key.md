---
layout: page
title: linux/apt-key (català)
description: "Eina de gestió de claus per al Gestor de Paquets APT (APT Package Manager) en Debian i Ubuntu."
content_hash: a944509fc9548eb2307d0c91799d7f742801a340
last_modified_at: 2024-09-18
related_topics:
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
  - title: polski version
    url: /pl/linux/apt-key.html
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

Eina de gestió de claus per al Gestor de Paquets APT (APT Package Manager) en Debian i Ubuntu.
Nota: `apt-key` és obsolet (excepte l'ús de `apt-key del` en scrits de mantenidor).
Més informació: <https://manned.org/apt-key.8>.

- Mostra les claus de confiança:

`apt-key list`

- Afegeix una clau al magatzem de claus de confiança:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arxiu_clau_pública.asc</span>

- Borra una clau del magatzem de claus de confiança:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_clau</span>

- Afegir una clau remota al magatzem de claus de confiança:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/archiu.clau</span>` | apt-key add -`

- Afegir una clau d'un servidor de claus amb l'identificador de la clau:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_clau</span>
