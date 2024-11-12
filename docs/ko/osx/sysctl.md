---
layout: page
title: osx/sysctl (한국어)
description: "커널 상태 정보를 확인합니다."
content_hash: 04c73ddc2410796a34c5082be4ec9f4dd7b55a9e
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/sysctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/sysctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sysctl

커널 상태 정보를 확인합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/sysctl.8.html>.

- 사용 가능한 모든 변수와 값 표시:

`sysctl -a`

- Apple 모델 식별자 표시:

`sysctl -n hw.model`

- CPU 모델 표시:

`sysctl -n machdep.cpu.brand_string`

- 사용 가능한 CPU 기능(MMX, SSE, SSE2, SSE3, AES 등) 표시:

`sysctl -n machdep.cpu.features`

- 변경 가능한 커널 상태 변수 설정:

`sysctl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section.tunable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
