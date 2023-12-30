---
layout: page
title: osx/terminal-notifier (español)
description: "Envía notificaciones de usuario en macOS."
content_hash: 3a95640c9dd4c4875b7fe01cdb2b96095789f89c
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/osx/terminal-notifier.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terminal-notifier

Envía notificaciones de usuario en macOS.
Más información: <https://github.com/julienXX/terminal-notifier>.

- Envía una notificación (sólo se necesita el mensaje):

`terminal-notifier -group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr-info</span>` -title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR</span>` -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR mola</span>`'`

- Muestra datos transmitidos con un sonido:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Datos de mensajes transmitidos!</span>`'' | terminal-notifier -sound `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- Abre una URL al hacer clic en la notificación:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Comprueba tus acciones de Apple!</span>`' -open '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://finance.yahoo.com/q?s=AAPL</span>`'`

- Abre una aplicación al hacer clic en la notificación:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Importados 42 contactos.</span>`'  -activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.AddressBook</span>
