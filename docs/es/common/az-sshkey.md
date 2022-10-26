---
layout: page
title: common/az-sshkey (español)
description: "Administra claves públicas SSH con máquinas virtuales."
content_hash: fdd61528eef24aaceb13da89fbccb2aa78391a3d
related_topics:
  - title: English version
    url: /en/common/az-sshkey.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az sshkey

Administra claves públicas SSH con máquinas virtuales.
Parte de `azure-cli`.
Más información: <https://learn.microsoft.com/cli/azure/sshkey>.

- Crea una nueva clave SSH:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>

- Sube una clave SSH existente:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --public-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@ruta/de/llave.pub</span>`"`

- Lista todas las claves públicas SSH:

`az sshkey list`

- Muestra información sobre una clave pública SSH:

`az sshkey show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>
