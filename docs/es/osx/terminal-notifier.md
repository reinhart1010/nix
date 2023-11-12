---
layout: page
title: osx/terminal-notifier (español)
description: "Envia notificaciones de usuario en macOS."
content_hash: 49e5b27a303fcfe84feca9681f7716a15b9bde4c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/terminal-notifier.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terminal-notifier

Envia notificaciones de usuario en macOS.
Más información: <https://github.com/julienXX/terminal-notifier>.

- Envia una notificación (sólo se requiere el mensaje):

`terminal-notifier -group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr-info</span>` -title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR</span>` -mensaje '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR mola</span>`'`

- Muestra datos canalizados con un sonido:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¡Datos de mensajes canalizados!</span>`'' | terminal-notifier -sound `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- Abre una URL al hacer clic en la notificación:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¡Comprueba tus acciones de Apple!</span>`' -open '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">! -open '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://finance.yahoo.com/q?s=AAPL</span>`'`

- Abre una aplicación al hacer clic en la notificación:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Se importaron 42 contactos.</span>`'  -activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.AddressBook</span>
