---
layout: page
title: osx/networkquality (한국어)
description: "인터넷에 연결하여 네트워크 품질을 측정합니다."
content_hash: 8b562e0a67be25002d28227cb9a37e7e118c1595
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/networkquality.html
    icon: bi bi-globe
tldri18n_status: 2
---
# networkQuality

인터넷에 연결하여 네트워크 품질을 측정합니다.
더 많은 정보: <https://support.apple.com/101942>.

- 기본 인터페이스의 네트워크 품질 테스트:

`networkQuality`

- 업로드 및 다운로드 속도를 병렬이 아닌 순차적으로 테스트:

`networkQuality -s`

- 지정한 네트워크 인터페이스 테스트:

`networkQuality -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>

- 자세한 출력을 통해 네트워크 품질 테스트:

`networkQuality -v`
