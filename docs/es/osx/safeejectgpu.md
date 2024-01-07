---
layout: page
title: osx/safeejectgpu (español)
description: "Expulsa una GPU de forma segura."
content_hash: ffdd2aceed14bf00a00bb995038361604fbc1eb4
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/osx/safeejectgpu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# SafeEjectGPU

Expulsa una GPU de forma segura.
Más información: <https://www.unix.com/man-page/mojave/8/safeejectgpu>.

- Expulsa todas las GPUs:

`SafeEjectGPU Eject`

- Lista todas las GPUs conectadas:

`SafeEjectGPU gpus`

- Lista de aplicaciones que utilizan una GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` apps`

- Obtén el estado de una GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` status`

- Expulsa una GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` Eject`

- Inicia una aplicación en una GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` LaunchOnGPU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/App.app</span>
