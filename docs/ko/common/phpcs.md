---
layout: page
title: common/phpcs (한국어)
description: "PHP, JavaScript 및 CSS 파일을 토큰화하여 정의된 코딩 표준 세트의 위반 사항을 감지합니다."
content_hash: b2186f9eae806351c8e06336e9d929ce32abf935
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/phpcs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/phpcs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpcs

PHP, JavaScript 및 CSS 파일을 토큰화하여 정의된 코딩 표준 세트의 위반 사항을 감지합니다.
더 많은 정보: <https://github.com/squizlabs/PHP_CodeSniffer>.

- 지정된 디렉터리를 검사하여 문제 탐지 (기본값은 PEAR 표준):

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 설치된 코딩 표준 목록 표시:

`phpcs -i`

- 검증할 코딩 표준 지정:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --standard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표준</span>

- 검사 시 포함할 확장자를 쉼표로 구분하여 지정:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_확장자1,파일_확장자2,...</span>

- 출력 보고서 형식 지정 (예: `full`, `xml`, `json`, `summary`):

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>

- 프로세스 중 사용할 설정 변수 설정:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --config-set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 처리 전에 로드할 파일의 쉼표로 구분된 목록:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --bootstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1,경로/대상/파일2,...</span>

- 하위 디렉토리로 재귀 탐색하지 않음:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -l`
