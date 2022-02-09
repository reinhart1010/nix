---
layout: page
title: linux/apt (català)
description: "Eina de gestió de paquets per a distribucions basades en Debian."
content_hash: c5a7199f13625da53c364a2dbaa170cc23519833
related_topics:
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
---
# apt

Eina de gestió de paquets per a distribucions basades en Debian.
Es recomana substituïr-lo per `apt-get` quan es faci servir interactivament en Ubuntu 16.04 o en versions posteriors.
Més informació: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Actualitza la llista de paquets i versions disponbles (es recomana executar aquest comandament abans que qualsevol altre `apt`):

`sudo apt update`

- Busca un paquet:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Mostra la informació de un paquet:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Instala un paquet o l'actualitza a l'última versió disponible:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Elimina un paquet (si s'utiliza `purge` també elimina els seus arxius de configuració):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Actualitza tots els paquets instal·lats a les noves versions disponibles:

`sudo apt upgrade`

- Mostra tots els paquets:

`apt list`

- Mostra tots els paquets instalats:

`apt list --installed`
