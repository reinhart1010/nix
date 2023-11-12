---
layout: page
title: osx/csshx (español)
description: "Herramienta SSH de clúster para macOS."
content_hash: 092741156b233dbf0e30a26b402624aa3b39e977
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/csshx.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/csshx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csshX

Herramienta SSH de clúster para macOS.
Más información: <https://github.com/brockgr/csshx>.

- Conectarse a múltiples hosts:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombrehost1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombrehost2</span>

- Conectarse a múltiples hosts con una clave SSH dada:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario@nombrehost1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario@nombrehost2</span>` --ssh_args "-i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_clave.pem</span>`"`

- Conectarse a un clúster predefinido desde `/etc/clusters`:

`csshX cluster1`
