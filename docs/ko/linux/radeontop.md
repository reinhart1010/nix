---
layout: page
title: linux/radeontop (한국어)
description: "AMD GPU의 사용률을 표시합니다."
content_hash: 38e6e3e4ca906a9cbff34d271f0de9e8e652afe2
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/radeontop.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/radeontop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# radeontop

AMD GPU의 사용률을 표시합니다.
시스템에 따라 루트 권한이 필요할 수 있습니다.
더 많은 정보: <https://github.com/clbr/radeontop>.

- 기본 AMD GPU의 사용률 표시:

`radeontop`

- 색상 출력 활성화:

`radeontop --color`

- 특정 GPU 선택 (버스 번호는 `lspci` 출력의 첫 번째 숫자입니다):

`radeontop --bus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스_번호</span>

- 화면 새로고침 빈도 지정 (값이 클수록 GPU 오버헤드가 증가):

`radeontop --ticks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초당_샘플_수</span>
