---
layout: page
title: common/lpq (한국어)
description: "프린터 대기열 상태 표시."
content_hash: 710a0d94cf45432ddff72045b979188ecfd28ff6
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lpq.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpq

프린터 대기열 상태 표시.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpq.html>.

- 기본 대상의 대기 중인 작업 표시:

`lpq`

- 모든 프린터의 대기 중인 작업을 암호화 적용하여 표시:

`lpq -a -E`

- 대기 중인 작업을 자세한 형식으로 표시:

`lpq -l`

- 특정 프린터나 클래스의 대기 중인 작업 표시:

`lpq -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상[/인스턴스]</span>

- 대기열이 비어질 때까지 n초마다 한 번씩 대기 중인 작업 표시:

`lpq +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">간격</span>
