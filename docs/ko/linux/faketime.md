---
layout: page
title: linux/faketime (한국어)
description: "명령어에 대해 시스템 시간을 속입니다."
content_hash: 0bfda7f45d3c84f35eac47c7fa6df4839e86762c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/faketime.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/faketime.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># faketime

명령어에 대해 시스템 시간을 속입니다.
더 많은 정보: <https://manned.org/faketime>.

- `date` 명령의 결과를 출력하기 전에 시간을 오늘 저녁으로 설정:

`faketime '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today 23:30</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">date</span>

- 어제를 현재 날짜로 사용하는 새로운 Bash 셸 열기:

`faketime '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yesterday</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- 다음 주 금요일 밤에 프로그램이 어떻게 작동할지 시뮬레이션:

`faketime '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">next Friday 1 am</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로그램</span>
