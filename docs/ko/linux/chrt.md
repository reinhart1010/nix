---
layout: page
title: linux/chrt (한국어)
description: "프로세스의 실시간 속성을 조작합니다."
content_hash: 1701dd6173ef91e30abedacd0479b8a4d1516423
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/chrt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chrt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chrt

프로세스의 실시간 속성을 조작합니다.
더 많은 정보: <https://manned.org/chrt>.

- 프로세스의 속성 표시:

`chrt --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 프로세스의 모든 스레드 속성 표시:

`chrt --all-tasks --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- `chrt`와 함께 사용할 수 있는 최소/최대 우선순위 값 표시:

`chrt --max`

- 프로세스의 스케줄링 우선순위 설정:

`chrt --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 프로세스의 스케줄링 정책 설정:

`chrt --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deadline|idle|batch|rr|fifo|other</span>` --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
