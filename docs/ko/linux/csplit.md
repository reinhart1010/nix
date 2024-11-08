---
layout: page
title: linux/csplit (한국어)
description: "파일을 여러 조각으로 분할합니다."
content_hash: 3b2e6dde6fc79aba1122596fc7b5b9edc02515d4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/csplit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/csplit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/csplit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/csplit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># csplit

파일을 여러 조각으로 분할합니다.
"xx00", "xx01" 등의 이름으로 파일을 생성합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/csplit>.

- 파일을 5번째 및 23번째 줄에서 분할:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 23`

- 파일을 5줄마다 분할 (총 줄 수가 5로 나누어 떨어지지 않으면 실패):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 {*}`

- 정확한 나누기 오류를 무시하고 파일을 5줄마다 분할:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 {*}`

- 5번째 줄에서 파일을 분할하고 출력 파일에 사용자 지정 접두사를 사용:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>

- 정규 표현식과 일치하는 줄에서 파일을 분할:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`/`
