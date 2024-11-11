---
layout: page
title: linux/showkey (한국어)
description: "키보드에서 누른 키의 키코드를 표시하여 키보드 관련 문제 디버깅 및 키 매핑에 유용합니다."
content_hash: ab6894ef719ec59b6934310d258280023ddeb5e0
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/showkey.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/showkey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/showkey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># showkey

키보드에서 누른 키의 키코드를 표시하여 키보드 관련 문제 디버깅 및 키 매핑에 유용합니다.
더 많은 정보: <https://manned.org/showkey>.

- 키코드를 10진수로 보기:

`sudo showkey`

- 스캔코드를 16진수로 표시:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--scancodes</span>

- 키코드를 10진수로 표시 (기본값):

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keycodes</span>

- 키코드를 ASCII, 10진수, 16진수로 표시:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--ascii</span>

- 프로그램 종료:

`Ctrl + d`
