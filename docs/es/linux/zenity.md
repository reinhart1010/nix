---
layout: page
title: linux/zenity (español)
description: "Muestra diálogos desde guiones de la línea de comandos."
content_hash: e5f7ef60f27ac0e3a7fb29d82f60f274ae4cc2c9
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/zenity.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/zenity.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zenity.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zenity

Muestra diálogos desde guiones de la línea de comandos.
Regresa los valores suministrados por el usuario o 1 si hay error.
Más información: <https://manned.org/zenity>.

- Muestra el diálogo predeterminado de pregunta:

`zenity --question`

- Muestra un diálogo de información que muestra el texto "¡Hola!":

`zenity --info --text="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¡Hola!</span>`"`

- Muestra un formulario  de nombre/contraseña y retorna los datos separados por ";":

`zenity --forms --add-entry="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Nombre</span>`" --add-password="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Contraseña</span>`" --separator="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`"`

- Muestra un formulario de selección de archivos en el que el usuario sólo puede seleccionar directorios:

`zenity --file-selection --directory`

- Muestra una barra de progreso que actualiza su mensaje cada segundo y muestra un porcentaje de progreso:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")</span>` | zenity --progress`
