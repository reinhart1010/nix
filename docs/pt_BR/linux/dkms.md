---
layout: page
title: linux/dkms (português (Brasil))
description: "Um framework que permite recompilação dinâmica de modulos do kernel."
content_hash: daea538473b0f55116108029db621b085813ac8a
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/linux/dkms.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dkms

Um framework que permite recompilação dinâmica de modulos do kernel.
Mais informações: <https://github.com/dell/dkms>.

- Lista os módulos instalados atualmente:

`dkms status`

- Recompila todos os módulos para o kernel que está rodando atualmente:

`dkms autoinstall`

- Instala a versão 1.2.1 do módulo acpi_call para o kernel que está rodando atualmente:

`dkms install -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acpi_call</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.1</span>

- Remove a versão 1.2.1 do módulo acpi_call de todos os kernels:

`dkms remove -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acpi_call</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.1</span>` --all`
