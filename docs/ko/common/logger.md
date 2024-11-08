---
layout: page
title: common/logger (한국어)
description: "메시지를 syslog (/var/log/syslog)에 추가."
content_hash: e245d96e8218ae7185f1c1617297ef87f680e9e4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/logger.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/logger.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/logger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logger

메시지를 syslog (/var/log/syslog)에 추가.
더 많은 정보: <https://manned.org/logger>.

- 메시지를 syslog에 기록:

`logger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- `stdin`에서 입력을 받아 syslog에 기록:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그_항목</span>` | logger`

- 지정된 포트에서 실행 중인 원격 syslog 서버로 출력 전송. 기본 포트는 514:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그_항목</span>` | logger --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 기록된 모든 줄에 특정 태그 사용. 기본값은 로그인한 사용자 이름:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그_항목</span>` | logger --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 주어진 우선순위로 메시지 기록. 기본값은 `user.notice`. 모든 우선순위 옵션은 `man logger` 참조:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그_항목</span>` | logger --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.warning</span>
