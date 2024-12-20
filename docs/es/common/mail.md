---
layout: page
title: common/mail (español)
description: "El comando opera en el buzón de correo del usuario si no se da ningún argumento."
content_hash: 13da8e4d90959f0cad2b79a3eb4997c4542c85c0
last_modified_at: 2024-12-20
related_topics:
  - title: English version
    url: /en/common/mail.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mail

El comando opera en el buzón de correo del usuario si no se da ningún argumento.
Para enviar un correo electrónico, el cuerpo del mensaje se construye desde `stdin`.
Más información: <https://manned.org/mail>.

- Abre un prompt interactivo para revisar el correo personal:

`mail`

- Envía un mensaje de correo con CC opcional. La línea de comandos continúa después de presionar `<Intro>`. Ingresa el texto del mensaje (pueden ser varias líneas). Presiona `<Ctrl>-D` para indicar el final del texto del mensaje:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título del correo electrónico</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">para_usuario@example.com</span>` --cc="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cc_correo_electrónico</span>`"`

- Envía un correo electrónico que contiene el contenido de un archivo:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOSTNAME archivo.txt</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">para_usuario@example.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>

- Envía un archivo `tar.gz` como adjunto:

`tar cvzf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio1 ruta/al/directorio2</span>` | uuencode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.tar.gz</span>` | mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asunto</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a_usuario@example.com</span>
