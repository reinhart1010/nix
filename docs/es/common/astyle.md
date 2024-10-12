---
layout: page
title: common/astyle (español)
description: "Indentador, formateador y embellecedor de código fuente para los lenguajes de programación C, C++, C# y Java."
content_hash: 93c4f6b36b0279f60f45a85cd3250ed42157e874
last_modified_at: 2024-10-12
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
tldri18n_status: 2
---
# astyle

Indentador, formateador y embellecedor de código fuente para los lenguajes de programación C, C++, C# y Java.
Al ejecutarse, se crea una copia del archivo original con un ".orig" añadido al nombre del archivo original.
Más información: <https://astyle.sourceforge.net>.

- Aplica el estilo por defecto de 4 espacios por sangría y sin cambios de formato:

`astyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_origen</span>

- Aplica el estilo Java con llaves adjuntas:

`astyle --style=java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Aplica el estilo allman con llaves discontinuas:

`astyle --style=allman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Aplica una sangría personalizada utilizando espacios. Elige entre 2 y 20 espacios:

`astyle --indent=spaces=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_espacios</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Aplica una sangría personalizada utilizando tabuladores. Elige entre 2 y 20 tabulaciones:

`astyle --indent=tab=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_pestañas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
