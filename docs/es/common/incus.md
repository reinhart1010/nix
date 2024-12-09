---
layout: page
title: common/incus (español)
description: "Contenedor de sistemas y gestor de máquinas virtuales moderno, seguro y potente."
content_hash: 16bc29be0a24f206871b62e67b95f502f0bbb33f
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/common/incus.html
    icon: bi bi-globe
tldri18n_status: 2
---
# incus

Contenedor de sistemas y gestor de máquinas virtuales moderno, seguro y potente.
Más información: <https://linuxcontainers.org/incus/docs/main>.

- Lista todos los contenedores y máquinas virtuales (tanto en ejecución como detenidas):

`incus list`

- Crea un contenedor a partir de una imagen, con un nombre personalizado:

`incus create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Inicia o detiene un contenedor existente:

`incus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Abre un intérprete de comandos dentro de un contenedor en ejecución:

`incus shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Elimina un contenedor detenido:

`incus delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Extrae una imagen de un repositorio de imágenes (remoto) al local:

`incus copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remoto</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>` local:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen_personalizada</span>

- Lista todas las imágenes disponibles en el repositorio oficial `images:` remoto:

`incus image list images:`

- Lista todas las imágenes ya descargadas en el remoto `local:`:

`incus image list local:`
