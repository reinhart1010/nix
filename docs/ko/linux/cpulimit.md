---
layout: page
title: linux/cpulimit (한국어)
description: "다른 프로세스의 CPU 사용을 제한하는 도구."
content_hash: e75f22150f6fb37fa31a553b97f8a4fcf29820ea
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/cpulimit.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cpulimit.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cpulimit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpulimit

다른 프로세스의 CPU 사용을 제한하는 도구.
더 많은 정보: <https://cpulimit.sourceforge.net/>.

- PID 1234인 기존 프로세스의 CPU 사용을 25%로 제한:

`cpulimit --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25%</span>

- 실행 파일 이름으로 기존 프로그램의 CPU 사용 제한:

`cpulimit --exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- 주어진 프로그램을 실행하고 CPU 사용을 50%로 제한:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램 인수1 인수2 ...</span>

- 프로그램을 실행하고 CPU 사용을 50%로 제한하며 cpulimit을 백그라운드에서 실행:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --background -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 프로그램의 CPU 사용이 50%를 초과하면 프로세스 종료:

`cpulimit --limit 50 --kill -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 프로그램과 자식 프로세스의 CPU 사용을 각각 25%로 제한:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` --monitor-forks -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>
