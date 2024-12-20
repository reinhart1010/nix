---
layout: page
title: linux/brightnessctl (español)
description: "Utilidad para leer y controlar el brillo de dispositivos en sistemas operativos Linux."
content_hash: 3b47d3248ddb6421541d03564f8f819e814a50dd
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/linux/brightnessctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/brightnessctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/brightnessctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/brightnessctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brightnessctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brightnessctl

Utilidad para leer y controlar el brillo de dispositivos en sistemas operativos Linux.
Más información: <https://github.com/Hummer12007/brightnessctl>.

- Lista de dispositivos a los que se les puede cambiar el brillo:

`brightnessctl --list`

- Imprime el brillo actual de la luz trasera de la pantalla:

`brightnessctl get`

- Establece el brillo de la luz trasera de la pantalla a un porcentaje en el rango válido:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>

- Aumenta el brillo con un incremento específico:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+10%</span>

- Disminuye el brillo con un decremento específico:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
