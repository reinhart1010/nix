---
layout: page
title: linux/strip (한국어)
description: "실행 파일이나 객체 파일에서 심볼을 제거합니다."
content_hash: dede5b4c93e903bd70df2e62929723d31bda66ed
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/strip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/strip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># strip

실행 파일이나 객체 파일에서 심볼을 제거합니다.
더 많은 정보: <https://manned.org/strip>.

- 입력 파일을 심볼이 제거된 버전으로 대체:

`strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 심볼을 제거하고, 출력을 특정 파일에 저장:

`strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 디버그 심볼만 제거:

`strip --strip-debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.o</span>
