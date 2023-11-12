---
layout: page
title: common/krunvm (español)
description: "Utilidad basada en CLI para crear micro máquinas virtuales utilizando imagenes OCI."
content_hash: dc8142d7260c5637f067e2f046ff55f109021863
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/krunvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# krunvm

Utilidad basada en CLI para crear micro máquinas virtuales utilizando imagenes OCI.
Más información: <https://github.com/containers/krunvm>.

- Crea una micro máquina virtual basada en Fedora:

`krunvm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker.io/fedora</span>` --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_vcpus</span>` --mem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memoria_en_megabytes</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`"`

- Inicia una imagen especifica:

`krunvm start "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`"`

- Lista las imagenes existentes:

`krunvm list`

- Cambia una imagen especifica:

`krunvm changevm --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_vcpus</span>` --mem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memoria_en_megabytes</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_nombre</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`"`

- Borra una imagen especifica:

`krunvm delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`"`
