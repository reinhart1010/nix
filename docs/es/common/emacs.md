---
layout: page
title: common/emacs (español)
description: "El editor extensible, personalizable, autodocumentado, en tiempo real."
content_hash: 04c23d80c6bb83bc12aa573a296fa4f76ad45992
last_modified_at: 2024-12-21
related_topics:
  - title: Deutsch version
    url: /de/common/emacs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/emacs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/emacs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/emacs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emacs

El editor extensible, personalizable, autodocumentado, en tiempo real.
Véase también `emacsclient`.
Más información: <https://www.gnu.org/software/emacs>.

- Inicia Emacs y abre un archivo:

`emacs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo en un número de línea especificado:

`emacs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Ejecuta un archivo Emacs Lisp como guión (script):

`emacs --script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.el</span>

- Inicia Emacs en modo consola (sin una ventana X):

`emacs --no-window-system`

- Inicia un servidor Emacs en segundo plano (accesible a través de `emacsclient`):

`emacs --daemon`

- Detiene un servidor Emacs en funcionamiento y todas sus instancias, pidiendo confirmación en archivos no guardados:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Guarda un archivo en Emacs:

`<Ctrl> + X, <Ctrl> + S`

- Sale de Emacs:

`<Ctrl> + X, <Ctrl> + C`
