---
layout: page
title: common/sv (한국어)
description: "실행 중인 runsv 서비스를 제어."
content_hash: 8b353a649fbc376825da17c6fa2f06e5cc9e28e2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/sv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sv

실행 중인 runsv 서비스를 제어.
더 많은 정보: <https://manned.org/sv.8>.

- 서비스 시작:

`sudo sv up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>

- 서비스 중지:

`sudo sv down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>

- 서비스 상태 확인:

`sudo sv status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>

- 서비스 다시 로드:

`sudo sv reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>

- 서비스를 시작하되, 실행 중이지 않은 경우에만 시작하고 중지되면 다시 시작하지 않음:

`sudo sv once `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>
