---
layout: page
title: linux/apt-key (català)
description: "Eina de gestió de claus per al Gestor de Paquets APT (APT Package Manager) en Debian i Ubuntu."
content_hash: 839cc4407875a26ba0513321206056df5418e130
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
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
---
# apt-key

Eina de gestió de claus per al Gestor de Paquets APT (APT Package Manager) en Debian i Ubuntu.
Nota: `apt-key` és obsolet (excepte l'ús de `apt-key del` en scrits de mantenidor).
Més informació: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

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
