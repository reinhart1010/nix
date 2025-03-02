---
layout: page
title: common/vagrant-plugin (español)
description: "Gestiona los complementos de Vagrant."
content_hash: a3da8a34b2d0471ebaba69ed7010b45e96b8e980
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/vagrant-plugin.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vagrant-plugin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vagrant plugin

Gestiona los complementos de Vagrant.
Vea también: `vagrant`.
Más información: <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- Lista todos los complementos actualmente instalados:

`vagrant plugin list`

- Instala un complemento desde repositorios remotos, normalmente RubyGems:

`vagrant plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>

- Instala un complemento desde un archivo local:

`vagrant plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/mi_complemento.gem</span>

- Actualiza todos los complementos instalados a su última versión:

`vagrant plugin update`

- Actualiza un complemento a la última versión:

`vagrant plugin update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>

- Desinstala un complemento específico:

`vagrant plugin uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>
