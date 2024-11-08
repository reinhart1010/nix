---
layout: page
title: linux/as (한국어)
description: "휴대용 GNU 어셈블러."
content_hash: de9223f45aa3fd8eacb1001acdb49937bc591d84
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/as.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/as.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/as.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/as.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/as.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># as

휴대용 GNU 어셈블러.
주로 `gcc`의 출력을 어셈블하여 `ld`에서 사용하도록 설계되었습니다.
더 많은 정보: <https://manned.org/as>.

- 파일을 어셈블하여 `a.out`으로 출력:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.s</span>

- 지정된 파일로 출력 어셈블:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.o</span>

- 공백 및 주석 전처리를 건너뛰어 더 빠르게 출력 생성 (신뢰할 수 있는 컴파일러에만 사용해야 함):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.s</span>

- `.include` 지시문에 지정된 파일을 검색할 디렉토리 목록에 주어진 경로 포함:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.s</span>
