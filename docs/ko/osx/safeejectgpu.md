---
layout: page
title: osx/safeejectgpu (한국어)
description: "GPU를 안전하게 제거합니다."
content_hash: 251b8e346c65ede8c8459fab985db942ea6418e4
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/safeejectgpu.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/safeejectgpu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# SafeEjectGPU

GPU를 안전하게 제거합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/SafeEjectGPU.8.html>.

- 모든 GPU 제거:

`SafeEjectGPU Eject`

- 연결된 모든 GPU 나열:

`SafeEjectGPU gpus`

- GPU를 사용하는 앱 나열:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` apps`

- GPU의 상태 확인:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` status`

- GPU 제거:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` Eject`

- GPU에서 앱 실행:

`SafeEjectGPU gpuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPU_ID</span>` LaunchOnGPU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/App.app</span>
