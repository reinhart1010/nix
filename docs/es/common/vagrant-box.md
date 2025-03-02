---
layout: page
title: common/vagrant-box (español)
description: "Administra cajas Vagrant (imágenes de máquinas virtuales)."
content_hash: ac89c57dd3e19b90563360c388a65426bbc2ec61
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/vagrant-box.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vagrant box

Administra cajas Vagrant (imágenes de máquinas virtuales).
Vea también: `vagrant`.
Más información: <https://developer.hashicorp.com/vagrant/docs/cli/box>.

- Lista todas las cajas instaladas:

`vagrant box list`

- Añade una nueva caja:

`vagrant box add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hashicorp/bionic64</span>

- Añade una caja desde una URL personalizada:

`vagrant box add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mi-caja</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/mi-caja.box</span>

- Elimina una caja instalada:

`vagrant box remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hashicorp/bionic64</span>

- Actualiza todas las cajas que están en uso en el entorno Vagrant actual:

`vagrant box update`

- Actualiza una caja específica:

`vagrant box update --box `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bento/debian-12</span>

- Comprueba si hay una nueva versión disponible para la caja que está usando:

`vagrant box outdated`

- Limpia las versiones antiguas de las cajas instaladas:

`vagrant box prune`
