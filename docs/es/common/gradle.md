---
layout: page
title: common/gradle (español)
description: "Un sistema de automatización de construcción de código abierto."
content_hash: 164de145ea9995ca1ec2cd2f9a000a1c2a5634a0
last_modified_at: 2023-12-20
related_topics:
  - title: English version
    url: /en/common/gradle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gradle

Un sistema de automatización de construcción de código abierto.
Más información: <https://gradle.org>.

- Compila un paquete:

`gradle build`

- Excluye la compilación test:

`gradle build -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test</span>

- Ejecuta en modo sin conexión para evitar que Gradle acceda a la red durante la compilación:

`gradle build --offline`

- Limpiar el directorio de compilación:

`gradle clean`

- Construye un paquete Android (APK) en modo release:

`gradle assembleRelease`

- Lista las tareas principales:

`gradle tasks`

- Lista todas las tareas:

`gradle tasks --all`
