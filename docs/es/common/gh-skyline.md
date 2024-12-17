---
layout: page
title: common/gh-skyline (español)
description: "Genera un modelo 3D de tu historial de contribuciones a GitHub."
content_hash: 42e0f88f9c4deea37004847f703328a783dda22c
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/common/gh-skyline.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh skyline

Genera un modelo 3D de tu historial de contribuciones a GitHub.
Por defecto, creará un archivo `{usuario}-{año}-github-skyline.stl` en el directorio actual.
Más información: <https://github.com/github/gh-skyline>.

- Genera un archivo STL de la línea del horizonte para el año actual y el usuario autenticado:

`gh skyline`

- Genera una línea del horizonte para un [u]suario y un año [y] específicos:

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">año</span>

- Genera una línea del horizonte para un intervalo de [a]ños:

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primer_año</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">último_año</span>

- Genera una línea del horizonte completa [f] (desde el año de alta del usuario hasta el año actual):

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --full`

- Habilita el registro de [d]epuración:

`gh skyline --debug`

- Genera una línea del horizonte y especifica la ruta del archivo de salida:

`gh skyline --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.stl</span>

- Abre el perfil de GitHub de un [u]suario específico:

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --web`

- Muestra ayuda:

`gh skyline --help`
