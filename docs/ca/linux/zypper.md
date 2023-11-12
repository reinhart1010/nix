---
layout: page
title: linux/zypper (català)
description: "Utilitat per la gestió de paquets en SUSE i openSUSE."
content_hash: 768631caa241c6bc6fa5ebf0d12753eb9bbe05e9
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zypper

Utilitat per la gestió de paquets en SUSE i openSUSE.
Més informació: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincronitza la llista de paquets i versions disponibles:

`zypper refresh`

- Instal·la un nou paquet:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Elimina un paquet:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Actualitza els paquets instal·lats a la versió més recent disponible:

`zypper update`

- Busca en els repositoris un paquet mitjançant una paraula clau:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paraula_clau</span>

- Mostra informació relacionada amb els repositoris configurats:

`zypper repos --sort-by-priority`
