---
layout: page
title: common/nms (한국어)
description: "1992년 영화 Sneakers에서 볼 수 있는 유명한 데이터 해독 효과를 `stdin`에서 재현하는 명령줄 도구."
content_hash: e209e8111d25d7fd520067cab15f2483b274e925
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nms.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nms.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nms

1992년 영화 Sneakers에서 볼 수 있는 유명한 데이터 해독 효과를 `stdin`에서 재현하는 명령줄 도구.
더 많은 정보: <https://github.com/bartobri/no-more-secrets>.

- 키 입력 후 텍스트 해독:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello, World!</span>`" | nms`

- 키 입력을 기다리지 않고 즉시 출력 해독:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -la</span>` | nms -a`

- 파일의 내용을 해독하고, 사용자 지정 출력 색상 사용:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | nms -a -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue|white|yellow|black|magenta|green|red</span>

- 해독하기 전에 화면 지우기:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | nms -a -c`
