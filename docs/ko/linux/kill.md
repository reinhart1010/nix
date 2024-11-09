---
layout: page
title: linux/kill (한국어)
description: "프로세스에 신호를 보내는 유틸리티로, 주로 프로세스 중지와 관련이 있습니다."
content_hash: 16765a58d808f54f45770a64bc856728e4b3d97a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/kill.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/kill.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/kill.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kill.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kill

프로세스에 신호를 보내는 유틸리티로, 주로 프로세스 중지와 관련이 있습니다.
SIGKILL 및 SIGSTOP을 제외한 모든 신호는 프로세스에 의해 가로채져서 안전하게 종료될 수 있습니다.
더 많은 정보: <https://manned.org/kill>.

- 기본 SIGTERM (종료) 신호를 사용하여 프로그램 종료:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 신호 값과 해당 이름 목록 표시 (`SIG` 접두사를 제외하고 사용):

`kill -L`

- 백그라운드 작업 종료:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- SIGHUP (연결 끊김) 신호를 사용하여 프로그램 종료. 많은 데몬이 종료 대신 다시 로드됩니다:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- SIGINT (인터럽트) 신호를 사용하여 프로그램 종료. 일반적으로 사용자가 `Ctrl + C`를 누를 때 시작됩니다:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 운영 체제에 프로그램을 즉시 종료하도록 신호 (프로세스가 신호를 캡처할 기회가 없음):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 운영 체제에 SIGCONT ("계속") 신호를 받을 때까지 프로그램을 일시 중지하도록 신호:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 주어진 GID (그룹 ID)를 가진 모든 프로세스에 `SIGUSR1` 신호 보내기:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_ID</span>
