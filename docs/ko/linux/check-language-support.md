---
layout: page
title: linux/check-language-support (한국어)
description: "Ubuntu에서 누락된 언어 패키지 목록을 표시합니다."
content_hash: ab504137c18d79ce7e2e8c805742f4f909dd4278
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/check-language-support.html
    icon: bi bi-globe
tldri18n_status: 2
---
# check-language-support

Ubuntu에서 누락된 언어 패키지 목록을 표시합니다.
더 많은 정보: <https://manned.org/check-language-support>.

- 설치된 소프트웨어와 활성화된 로케일을 기반으로 누락된 언어 패키지 목록 표시:

`check-language-support`

- 특정 로케일의 패키지 나열:

`check-language-support --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>

- 설치된 패키지와 누락된 패키지 모두 표시:

`check-language-support --show-installed`
