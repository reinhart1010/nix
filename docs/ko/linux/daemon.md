---
layout: page
title: linux/daemon (한국어)
description: "프로세스를 데몬으로 실행."
content_hash: f62b723b6b4b4afa6792a6b09057cacda9d520db
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/daemon.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/daemon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/daemon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># daemon

프로세스를 데몬으로 실행.
더 많은 정보: <https://manned.org/daemon>.

- 명령어를 데몬으로 실행:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령어를 데몬으로 실행하고, 충돌 시 재시작:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" --respawn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 충돌 시 재시작하는 데몬으로 명령어를 실행하며, 10초마다 두 번 시도:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" --respawn --attempts=2 --delay=10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 로그를 특정 파일에 기록하며 명령어를 데몬으로 실행:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" --errlog=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 데몬 종료 (SIGTERM):

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" --stop`

- 데몬 목록 나열:

`daemon --list`
