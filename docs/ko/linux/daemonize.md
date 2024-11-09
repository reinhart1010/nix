---
layout: page
title: linux/daemonize (한국어)
description: "유닉스 데몬으로 명령어(자체적으로 데몬화하지 않는)를 실행합니다."
content_hash: a658ae37bd33a0346fc0238c489c132c70bbd725
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/daemonize.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/daemonize.html
    icon: bi bi-globe
tldri18n_status: 2
---
# daemonize

유닉스 데몬으로 명령어(자체적으로 데몬화하지 않는)를 실행합니다.
더 많은 정보: <https://software.clapper.org/daemonize/>.

- 명령어를 데몬으로 실행:

`daemonize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- PID를 지정된 파일에 작성:

`daemonize -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/PID_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- 락 파일을 사용하여 한 번에 하나의 인스턴스만 실행되도록 보장:

`daemonize -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/락_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- 지정된 사용자 계정을 사용:

`sudo daemonize -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>
