---
layout: page
title: linux/systemd-hwdb (한국어)
description: "하드웨어 데이터베이스 관리 도구."
content_hash: 7a40cbccedb48ac4f8c6181a4ecdd2213b14a5f5
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-hwdb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-hwdb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-hwdb

하드웨어 데이터베이스 관리 도구.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-hwdb.html>.

- `/etc/udev`의 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb update`

- 하드웨어 데이터베이스를 조회하고 특정 모달리아스에 대한 결과 출력:

`systemd-hwdb query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모달리아스</span>

- 구문 오류 발생 시 0이 아닌 종료 값을 반환하며 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb --strict update`

- `/usr/lib/udev`의 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb --usr update`

- 지정된 루트 경로의 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/루트</span>` update`
