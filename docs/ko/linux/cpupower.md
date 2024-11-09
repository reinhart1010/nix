---
layout: page
title: linux/cpupower (한국어)
description: "CPU 전력 및 조정 옵션 관련 도구."
content_hash: 337f9cc51a3903c84e3de1732e1a079e2a138eab
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cpupower.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpupower

CPU 전력 및 조정 옵션 관련 도구.
더 많은 정보: <https://manned.org/cpupower>.

- CPU 목록 나열:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` info`

- 모든 코어에 대한 정보 출력:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` info`

- 모든 CPU를 절전 주파수 관리자로 설정:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` frequency-set --governor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">powersave</span>

- CPU 0의 사용 가능한 주파수 [g]overnor 출력:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` frequency-info g | grep "analyzing\|governors"`

- CPU 4의 하드웨어 주파수를 사람이 읽기 쉬운 형식으로 출력:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` frequency-info --hwfreq --human`
