---
layout: page
title: common/amass-enum (español)
description: "Busca subdominios de un dominio."
content_hash: 923b2aa5786716a689c210ab9b57067ad32d7301
last_modified_at: 2022-12-31
related_topics:
  - title: English version
    url: /en/common/amass-enum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-enum.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass enum

Busca subdominios de un dominio.
Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Búsqueda pasiva de subdominios de un dominio:

`amass enum -passive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>

- Busca subdominios de un dominio y los verifica activamente intentando resolver los subdominios encontrados:

`amass enum -active -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,8080</span>

- Hace una búsqueda en su modalidad fuerza bruta de subdominios:

`amass enum -brute -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>

- Guarda los resultados en un archivo de texto:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_salida</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>

- Guarda los resultados a una base de datos:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_salida</span>` -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_base_de_datos</span>
