---
layout: page
title: linux/perf (한국어)
description: "Linux 성능 카운터 측정을 위한 프레임워크."
content_hash: 3fb9e046466f40117be2ae9cb77fcfcecce40dbc
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/perf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/perf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># perf

Linux 성능 카운터 측정을 위한 프레임워크.
더 많은 정보: <https://perf.wiki.kernel.org>.

- 명령에 대한 기본 성능 카운터 통계 표시:

`perf stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc hello.c</span>

- 시스템 전역의 실시간 성능 카운터 프로필 표시:

`sudo perf top`

- 명령을 실행하고 프로필을 `perf.data`에 기록:

`sudo perf record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 기존 프로세스의 프로필을 `perf.data`에 기록:

`sudo perf record -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- `perf.data`( `perf record`에 의해 생성됨)를 읽고 프로필 표시:

`sudo perf report`
