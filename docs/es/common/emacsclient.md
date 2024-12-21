---
layout: page
title: common/emacsclient (español)
description: "Abre archivos en un servidor Emacs existente."
content_hash: 9fa988ce8237af4247eebf9b3dd383465172e49e
last_modified_at: 2024-12-21
related_topics:
  - title: Deutsch version
    url: /de/common/emacsclient.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/emacsclient.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacsclient.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/emacsclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emacsclient

Abre archivos en un servidor Emacs existente.
Vea también `emacs`.
Más información: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- Abre un archivo en un servidor Emacs existente (utilizando GUI si está disponible):

`emacsclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo en modo consola (sin una ventana X):

`emacsclient --no-window-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo en una nueva ventana Emacs:

`emacsclient --create-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Evalúa un comando, imprime la salida a `stdout`, y luego sale:

`emacsclient --eval '(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`)'`

- Especifica un editor alternativo en caso de que ningún servidor Emacs esté funcionando:

`emacsclient --alternate-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Detiene un servidor Emacs en funcionamiento y todas sus instancias, pidiendo confirmación en archivos no guardados:

`emacsclient --eval '(save-buffers-kill-emacs)'`
