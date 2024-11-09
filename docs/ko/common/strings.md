---
layout: page
title: common/strings (한국어)
description: "객체 파일이나 바이너리에서 출력 가능한 문자열을 찾습니다."
content_hash: be78e6efbe87a70e52e8c9d32cc5e9594ae70d47
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/strings.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/strings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/strings.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/strings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># strings

객체 파일이나 바이너리에서 출력 가능한 문자열을 찾습니다.
더 많은 정보: <https://manned.org/strings>.

- 바이너리의 모든 문자열 출력:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 결과를 최소 n 글자 이상의 문자열로 제한:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 결과 앞에 파일 내 오프셋 접두사 추가:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 결과 앞에 파일 내 오프셋을 16진수로 접두사 추가:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
