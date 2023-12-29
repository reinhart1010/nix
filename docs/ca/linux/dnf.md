---
layout: page
title: linux/dnf (català)
description: "Administrador de paquets per RHEL, CentOS i Fedora (Reemplaça a yum)."
content_hash: f586b6e6dd3eb44da3edeac68ae98ba7ba388fac
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dnf

Administrador de paquets per RHEL, CentOS i Fedora (Reemplaça a yum).
Més informació: <https://dnf.readthedocs.io>.

- Actualitza tots els paquets a l'última versió disponible:

`sudo dnf update`

- Busca un paquet fent servir paraules clau:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clau1 palabra_clau2 ...</span>

- Mostra informació sobre un paquet:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Instal·la un nou paquet:

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet1 paquet2 ...</span>

- Desinstal·la un paquet:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet1 paquet2 ...</span>

- Llista tots els paquets instal·lats:

`dnf list --installed`

- Troba quin paquet proveeeix un arxiu determinat:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arxiu</span>
