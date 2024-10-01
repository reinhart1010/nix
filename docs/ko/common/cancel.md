---
layout: page
title: common/cancel (한국어)
description: "프린트 작업 취소."
content_hash: 6fcaab44c44b1045b7e82ea3edd431688100edba
last_modified_at: 2024-10-01
related_topics:
  - title: English version
    url: /en/common/cancel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cancel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cancel

프린트 작업 취소.
참고: `lp`, `lpmove`, `lpstat`.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- 기본 프린터의 현재 작업을 취소 (`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>로 설정):

`cancel`

- 특정 사용자([u]ser)가 소유한 기본 프린터의 작업을 취소:

`cancel -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 프린터의 현재 작업을 취소:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>

- 특정 프린터에서 특정 작업을 취소:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 모든 프린터의 모든([a]ll) 작업을 취소:

`cancel -a`

- 특정 프린터의 모든([a]ll) 작업을 취소:

`cancel -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>

- 특정 서버의 현재 작업을 취소한 다음 작업 데이터 파일을 삭제([x]):

`cancel -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` -x`
