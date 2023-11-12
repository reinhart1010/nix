---
layout: page
title: linux/dnf (català)
description: "Administrador de paquets per RHEL, CentOS i Fedora (Reemplaça a yum)."
content_hash: a557e7689de0252b1450451603ae1de8adca7dc6
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# dnf

Administrador de paquets per RHEL, CentOS i Fedora (Reemplaça a yum).
Més informació: <https://dnf.readthedocs.io>.

- Actualitza tots els paquets a l'última versió disponible:

`sudo dnf update`

- Busca un paquet fent servir paraules clau:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clau</span>

- Mostra informació sobre un paquet:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Instal·la un nou paquet:

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Instal·la un nou paquet responent si a totes les preguntes:

`sudo dnf install -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Desinstal·la un paquet:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Llista tots els paquets instal·lats:

`dnf list --installed`

- Troba quin paquet proveeeix un arxiu determinat:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arxiu</span>
