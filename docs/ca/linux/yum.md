---
layout: page
title: linux/yum (català)
description: "Administrador de paquets per RHEL, CentOS i Fedora (per versions anteriors)."
content_hash: 3e5e227cc764f9639309ebee13e0aa1d95b5e099
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/yum.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/yum.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yum

Administrador de paquets per RHEL, CentOS i Fedora (per versions anteriors).
Més informació: <https://manned.org/yum>.

- Instal·la un nuevo paquete:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Instal·la un nou paquet responent si a totes les preguntes (també funciona amb actualitzacions, útil per actualitzacions automàtiques):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Troba quin paquet proveeix un arxiu determinat:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comandament</span>

- Elimina un paquet:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Mostra les actualitzacions disponibles per els paquets instal·lats:

`yum check-update`

- Actualitza els paquets instal·lats a les versions més recents disponibles:

`yum upgrade`
