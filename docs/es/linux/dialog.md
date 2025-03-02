---
layout: page
title: linux/dialog (español)
description: "Muestra cuadros de diálogo en el terminal."
content_hash: 5ee7f91a278fb63153ec56d61d36ac4454b361e8
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/linux/dialog.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dialog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dialog

Muestra cuadros de diálogo en el terminal.
Más información: <https://manned.org/dialog>.

- Muestra un mensaje:

`dialog --msgbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Mensaje</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">altura</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancho</span>

- Solicita ingreso de texto al usuario:

`dialog --inputbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ingrese texto:</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>` 2>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salida.txt</span>

- Solicitar al usuario una pregunta de sí/no:

`dialog --yesno "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¿Continuar?</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>
