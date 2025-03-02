---
layout: page
title: linux/opkg (español)
description: "Un gestor de paquetes ligero utilizado para instalar paquetes OpenWrt."
content_hash: 93a72f23e9bf3665e7cf2bd96e1b3a39ff779e3f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/opkg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/opkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opkg

Un gestor de paquetes ligero utilizado para instalar paquetes OpenWrt.
Más información: <https://openwrt.org/docs/guide-user/additional-software/opkg>.

- Instala un paquete:

`opkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete:

`opkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza la lista de paquetes disponibles:

`opkg update`

- Actualiza uno o varios paquetes específicos:

`opkg upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete(s)</span>

- Muestra información sobre un paquete concreto:

`opkg info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista todos los paquetes disponibles:

`opkg list`

- Averigua a qué paquete pertenece un archivo:

`opkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista todos los archivos de un paquete:

`opkg files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>
