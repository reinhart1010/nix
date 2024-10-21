---
layout: page
title: common/forever (한국어)
description: "Node.js 애플리케이션이 무기한 실행되도록 하는 서버측 JavaScript 애플리케이션 (종료 후 다시 시작됨)."
content_hash: 3d4c405a6874371344f00e25a3383a34304d011b
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/forever.html
    icon: bi bi-globe
tldri18n_status: 2
---
# forever

Node.js 애플리케이션이 무기한 실행되도록 하는 서버측 JavaScript 애플리케이션 (종료 후 다시 시작됨).
더 많은 정보: <https://github.com/foreversd/forever>.

- 파일을 무기한으로 실행하기 시작 (데몬으로):

`forever `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>

- 실행중인 "영원한" 프로세스 목록 ("영원한" 프로세스의 ID 및 기타 세부정보와 함께):

`forever list`

- 실행 중인 "영구" 프로세스를 중지:

`forever stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID|pid|script</span>
