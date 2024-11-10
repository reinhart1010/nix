---
layout: page
title: linux/top (한국어)
description: "실행 중인 프로세스에 대한 동적 실시간 정보를 표시합니다."
content_hash: e1da69dac234100e271ef73720264422a2a34d62
last_modified_at: 2024-11-10
related_topics:
  - title: català version
    url: /ca/linux/top.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/top.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/top.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

실행 중인 프로세스에 대한 동적 실시간 정보를 표시합니다.
더 많은 정보: <https://manned.org/top>.

- `top` 시작:

`top`

- 유휴 또는 좀비 프로세스를 표시하지 않음:

`top -i`

- 특정 사용자 소유의 프로세스만 표시:

`top -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 필드로 프로세스 정렬:

`top -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름</span>

- 특정 프로세스의 개별 스레드 표시:

`top -Hp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 쉼표로 구분된 목록으로 전달된 특정 PID의 프로세스만 표시 (일반적으로 PID를 즉석에서 알 수 없습니다. 이 예는 프로세스 이름에서 PID를 선택합니다):

`top -p $(pgrep -d ',' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>`)`

- 대화형 명령에 대한 도움말 표시:

`?`
