---
layout: page
title: linux/autorandr (español)
description: "Cambia automáticamente la disposición de la pantalla."
content_hash: dd22609ddfda3db47e29ed678a2cb808ee2a5762
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/autorandr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/autorandr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/autorandr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/autorandr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autorandr

Cambia automáticamente la disposición de la pantalla.
Más información: <https://github.com/phillipberndt/autorandr>.

- Guarda la disposición actual de la pantalla:

`autorandr --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>

- Muestra los perfiles guardados:

`autorandr`

- Carga el primer perfil detectado:

`autorandr --change`

- Carga un perfil específico:

`autorandr --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>

- Establece el perfil predeterminado:

`autorandr --default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>
