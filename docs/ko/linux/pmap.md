---
layout: page
title: linux/pmap (한국어)
description: "프로세스 또는 프로세스들의 메모리 맵을 보고."
content_hash: 789fdbb33e288ec6aa68496cf9be5c1a7606e13c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pmap

프로세스 또는 프로세스들의 메모리 맵을 보고.
더 많은 정보: <https://manned.org/pmap>.

- 특정 프로세스 ID (PID)의 메모리 맵 출력:

`pmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 확장된 형식 표시:

`pmap --extended `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 장치 형식 표시:

`pmap --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- `low`와 `high`로 지정된 메모리 주소 범위로 결과 제한:

`pmap --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">high</span>

- 여러 프로세스의 메모리 맵 출력:

`pmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>
