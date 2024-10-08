---
layout: page
title: linux/apt-key (español)
description: "Herramienta para la gestión de claves para el Gestor de Paquetes APT (APT Package Manager) en Debian y Ubuntu."
content_hash: a091d593ded9a13a93d200d818826c40a61467a2
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

Herramienta para la gestión de claves para el Gestor de Paquetes APT (APT Package Manager) en Debian y Ubuntu.
Más información: <https://manned.org/apt-key.8>.

- Muestra las claves de confianza:

`apt-key list`

- Añade una clave al almacén de claves de confianza:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_clave_pública.asc</span>

- Borra una clave del almacén de claves de confianza:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_clave</span>

- Añade un clave remota al almacén de claves de confianza:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/archivo.clave</span>` | apt-key add -`

- Añade una clave de un servidor de claves con el identificador de la clave:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_clave</span>
