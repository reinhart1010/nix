---
layout: page
title: common/git-gui (español)
description: "Una GUI para Git para gestionar ramas, remotos, confirmaciones de cambio y realizar fusiones locales."
content_hash: 82263999e9e03296b15997090afb24ea7d2422c3
last_modified_at: 2024-02-21
related_topics:
  - title: English version
    url: /en/common/git-gui.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git gui

Una GUI para Git para gestionar ramas, remotos, confirmaciones de cambio y realizar fusiones locales.
Vea también: `git-cola`, `gitk`.
Más información: <https://git-scm.com/docs/git-gui>.

- Inicia la GUI:

`git gui`

- Muestra un archivo específico con el nombre del autor y el hash de confirmación en cada línea:

`git gui blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre `git gui blame` en una revisión específica:

`git gui blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisión</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre `git gui blame` y desplaza la vista para centrarla en una línea específica:

`git gui blame --line=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">línea</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre una ventana para hacer una confirmación y vuelve al intérprete de comandos cuando se haya completado:

`git gui citool`

- Abre `git gui citool` en modo "Modificar la última confirmación":

`git gui citool --amend`

- Abre `git gui citool` en modo de solo lectura:

`git gui citool --nocommit`

- Muestra un navegador para el árbol de una rama específica, abriendo la herramienta de autoría al hacer clic en los archivos:

`git gui browser maint`
