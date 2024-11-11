---
layout: page
title: linux/sar (한국어)
description: "다양한 Linux 하위 시스템의 성능을 모니터링합니다."
content_hash: 12753f8505f3bcd030fd3c3f5733e868b511aeec
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sar

다양한 Linux 하위 시스템의 성능을 모니터링합니다.
더 많은 정보: <https://manned.org/sar>.

- 물리적 장치에 발행된 I/O 및 전송 속도를 1초 간격으로 보고 (종료하려면 CTRL+C 입력):

`sar -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 네트워크 장치 통계를 2초 간격으로 총 10회 보고:

`sar -n DEV `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- CPU 사용률을 2초 간격으로 보고:

`sar -u ALL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 메모리 사용 통계를 1초 간격으로 총 20회 보고:

`sar -r ALL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- 실행 대기열 길이와 평균 부하를 1초 간격으로 보고:

`sar -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 페이징 통계를 5초 간격으로 보고:

`sar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
