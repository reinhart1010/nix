---
layout: page
title: common/cupsenable (한국어)
description: "프린터 및 프린터 클래스를 시작."
content_hash: 30683ca5b10d8d6bec67103fe38a74db375eff50
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cupsenable.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cupsenable.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsenable.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsenable

프린터 및 프린터 클래스를 시작.
참고: 목적지는 프린터 또는 프린터 클래스를 나타냄.
더 보기: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
더 많은 정보: <https://www.cups.org/doc/man-cupsenable.html>.

- 하나 이상의 목적지들을 시작:

`cupsenable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지1 목적지2 ...</span>

- 목적지의 보류 중인 작업 인쇄를 재개 (`--hold`와 함께 `cupsdisable` 뒤에 사용):

`cupsenable --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지</span>

- 지정된 목적지들의 모든 작업 취소:

`cupsenable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지1 목적지2 ...</span>
