---
layout: page
title: common/stressapptest (한국어)
description: "사용자 영역 메모리 및 IO 테스트."
content_hash: 0f406e16051e9d874aee1f398d1d0f81781abff0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stressapptest.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/stressapptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stressapptest

사용자 영역 메모리 및 IO 테스트.
더 많은 정보: <https://github.com/stressapptest/stressapptest>.

- 주어진 메모리 용량(메가바이트 단위)을 테스트:

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리</span>

- 메모리와 지정된 파일의 I/O를 테스트:

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 상세 수준을 지정하여 테스트 (0=최저, 20=최고, 8=기본):

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수준</span>
