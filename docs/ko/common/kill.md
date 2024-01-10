---
layout: page
title: common/kill (한국어)
description: "보통 프로세스를 정지시키는 것과 관련된 시그널을 전송합니다."
content_hash: 3cc7974cde9bb163606650ce467f95f8ee34a90e
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/kill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kill.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/kill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kill.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kill

보통 프로세스를 정지시키는 것과 관련된 시그널을 전송합니다.
SIGKILL과 SIGSTOP을 제외한 모든 시그널들은 깔끔한 종료를 위해 프로세스에게 뺏길 수 있습니다.
더 많은 정보: <https://manned.org/kill.1posix>.

- 기본 SIGTERM ("terminate") 시그널을 보내 프로그램을 종료:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- 사용 가능한 시그널 이름을 출력 (`SIG` 접두사는 없이 출력):

`kill -l`

- 백그라운드 job 종료:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_아이디</span>

- SIGHUP ("hang up") 시그널을 사용해서 프로그램을 종료. 대다수의 데몬(백그라운드 프로세스)은 종료하는 대신 리로드 함:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- SIGINT ("interrupt") 시그널을 사용해서 프로그램을 종료. 이건 일반적으로 사용자가 `Ctrl + c`를 누를 때 일어나는 일과 같음:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- 운영체제에게 즉시 프로그램을 종료하라는 시그널을 전송 (프로세스가 신호를 받지 못하고 종료됨):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- 운영체제에게 SIGCONT ("continue") 시그널을 받기 전까지 프로그램을 일시정지하라는 시그널을 전송:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- 주어진 GID (그룹 아이디)를 가진 모든 프로세스에게 `SIGUSR1` 시그널을 전송:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>
