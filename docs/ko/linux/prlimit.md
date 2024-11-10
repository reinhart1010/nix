---
layout: page
title: linux/prlimit (한국어)
description: "프로세스 리소스의 소프트 및 하드 제한을 가져오거나 설정합니다."
content_hash: fc5b53a8164973386ee81df6036260394ec556a5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/prlimit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prlimit

프로세스 리소스의 소프트 및 하드 제한을 가져오거나 설정합니다.
프로세스 ID와 하나 이상의 리소스를 지정하면 prlimit이 제한을 검색 및/또는 수정하려고 시도합니다.
더 많은 정보: <https://manned.org/prlimit>.

- 실행 중인 부모 프로세스의 모든 현재 리소스 제한 값을 표시:

`prlimit`

- 지정된 프로세스의 모든 현재 리소스 제한 값을 표시:

`prlimit --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid_번호</span>

- 사용자 지정 열린 파일 수 제한으로 명령 실행:

`prlimit --nofile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
