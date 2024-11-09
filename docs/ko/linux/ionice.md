---
layout: page
title: linux/ionice (한국어)
description: "프로그램의 I/O 스케줄링 클래스 및 우선순위를 가져오거나 설정합니다."
content_hash: fd534e5940c1d1dc4e3ec13735c77487735545da
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ionice.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ionice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ionice

프로그램의 I/O 스케줄링 클래스 및 우선순위를 가져오거나 설정합니다.
스케줄링 클래스: 1 (실시간), 2 (최선 노력), 3 (유휴).
우선순위 수준: 0 (가장 높음) - 7 (가장 낮음).
더 많은 정보: <https://manned.org/ionice>.

- 주어진 스케줄링 클래스 및 우선순위로 명령 실행:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스케줄링_클래스</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 실행 중인 프로세스의 I/O 스케줄링 [c]클래스를 특정 [p]pid, [P]gid 또는 [u]uid로 설정:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스케줄링_클래스</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">p|P|u</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 사용자 정의 I/O 스케줄링 [c]클래스 및 우선순위로 명령 실행:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스케줄링_클래스</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 요청한 우선순위 설정에 실패하더라도 무시:

`ionice -t -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 원하는 우선순위를 설정할 수 없는 경우에도 명령 실행 (이 경우는 권한 부족 또는 오래된 커널 버전으로 인해 발생할 수 있음):

`ionice -t -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 실행 중인 프로세스의 I/O 스케줄링 클래스 및 우선순위 출력:

`ionice -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
