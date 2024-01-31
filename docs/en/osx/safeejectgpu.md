---
layout: page
title: osx/safeejectgpu (English)
description: "Eject a GPU safely."
content_hash: a372c113ca34607ab7a21b3ff4fd2a5e7c94102b
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/safeejectgpu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# SafeEjectGPU

Eject a GPU safely.
More information: <https://keith.github.io/xcode-man-pages/safeejectgpu.8.html>.

- Eject all GPUs:

`SafeEjectGPU Eject`

- List all GPUs attached:

`SafeEjectGPU gpus`

- List apps using a GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` apps`

- Get the status of a GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` status`

- Eject a GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` Eject`

- Launch an app on a GPU:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` LaunchOnGPU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/App.app</span>
