---
layout: page
title: linux/ntpq (한국어)
description: "네트워크 타임 프로토콜(NTP) 데몬 질의 도구."
content_hash: 7387e735bd57b9bcd1ccbe1adbeed13a3e1c1a20
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ntpq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ntpq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ntpq

네트워크 타임 프로토콜(NTP) 데몬 질의 도구.
더 많은 정보: <https://www.eecis.udel.edu/~mills/ntp/html/ntpq.html>.

- 대화형 모드로 `ntpq` 시작:

`ntpq --interactive`

- NTP 피어 목록 출력:

`ntpq --peers`

- IP 주소에서 호스트명을 해석하지 않고 NTP 피어 목록 출력:

`ntpq --numeric --peers`

- 디버깅 모드로 `ntpq` 사용:

`ntpq --debug-level`

- NTP 시스템 변수 값 출력:

`ntpq --command=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rv</span>
