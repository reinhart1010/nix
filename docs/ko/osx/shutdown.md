---
layout: page
title: osx/shutdown (한국어)
description: "시스템을 종료하고 재부팅합니다."
content_hash: 8b3c0500e0891d224a6e633c5c0c1bafea5ad710
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/shutdown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

시스템을 종료하고 재부팅합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/shutdown.8.html>.

- 즉시 시스템 전원 끄기 (정지):

`shutdown -h now`

- 즉시 절전 모드로 전환:

`shutdown -s now`

- 즉시 재부팅:

`shutdown -r now`

- 5분 후 재부팅:

`shutdown -r "+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`"`

- 오후 1시에 시스템 전원 끄기 (24시간 형식 사용):

`shutdown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1300</span>

- 2042년 5월 10일 오전 11시 30분에 재부팅 (입력 형식: YYMMDDHHMM):

`shutdown -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4205101130</span>
