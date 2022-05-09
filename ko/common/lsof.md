---
layout: page
title: common/lsof (한국어)
description: "열린 파일과 상응하는 프로세스들을 나열합니다."
content_hash: 220b5c31b3eacb70051e79c5fe5c41f55af58cf3
related_topics:
  - title: English version
    url: /en/common/lsof.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lsof.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsof

열린 파일과 상응하는 프로세스들을 나열합니다.
참고: 다른 사람으로부터 열린 파일 리스트는 루트 권한 ( 혹은 sudo ) 이 요구됩니다.
더 많은 정보: <https://manned.org/lsof>.

- 주어진 파일을 열고있는 프로세스 찾기:

`lsof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/의/경로</span>

- 로컬 인터넷 포트를 열고있는 프로세스 찾기:

`lsof -i :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 프로세스 아이디 (PID)만 출력:

`lsof -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/의/경로</span>

- 주어진 유저에 의해 열린 파일 나열:

`lsof -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유저이름</span>

- 주어진 명령어 혹은 프로세스에 의해 열린 파일 나열:

`lsof -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_혹은_명령어_이름</span>

- 주어진 PID와 일치하는 프로세스에 의해 열린 파일 나열:

`lsof -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 디렉토리 안의 열린 파일 나열:

`lsof +D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로</span>

- 로컬 IPv6 TCP 포트에서 수신 중이고 네트워크 또는 포트 번호를 변환하지 않는 프로세스 찾기:

`lsof -i6TCP:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -sTCP:LISTEN -n -P`
