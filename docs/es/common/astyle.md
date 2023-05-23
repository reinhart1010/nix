---
layout: page
title: common/astyle (español)
description: "Indentador, formateador y embellecedor de código fuente para los lenguajes de programación C, C++, C# y Java."
content_hash: f318ca1e0805fdf023f6a6ffde48a0c1658eee13
last_modified_at: 2023-05-20
related_topics:
  - title: English version
    url: /en/common/astyle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/astyle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/astyle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/astyle.html
    icon: bi bi-globe
---
# astyle

Indentador, formateador y embellecedor de código fuente para los lenguajes de programación C, C++, C# y Java.
Al ejecutarse, se crea una copia del archivo original con un ".orig" añadido al nombre del archivo original.
Más información: <http://astyle.sourceforge.net>.

- Aplica el estilo por defecto de 4 espacios por sangría y sin cambios de formato:

`estilo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_origen</span>

- Aplica el estilo Java con llaves adjuntas:

`astyle --style=java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Aplica el estilo allman con llaves discontinuas:

`astyle --style=allman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Aplica una sangría personalizada utilizando espacios. Elige entre 2 y 20 espacios:

`astyle --indent=spaces=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_espacios</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Aplica una sangría personalizada utilizando tabuladores. Elige entre 2 y 20 tabulaciones:

`astyle --indent=tab=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_pestañas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>