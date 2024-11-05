---
layout: page
title: common/phpstan (한국어)
description: "코드의 버그를 발견하기 위한 PHP 정적 분석 도구."
content_hash: cdc06ebc6c40faa464a413fad41b3ba32065fab4
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/phpstan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/phpstan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpstan

코드의 버그를 발견하기 위한 PHP 정적 분석 도구.
더 많은 정보: <https://github.com/phpstan/phpstan>.

- 하나 이상의 디렉터리 분석:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2 ...</span>

- 구성 파일을 사용하여 디렉터리 분석:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성</span>

- 특정 규칙 레벨을 사용하여 분석 (0-7, 숫자가 높을수록 엄격함):

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레벨</span>

- 분석 전에 로드할 자동 로드 파일 지정:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --autoload-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/자동로드_파일</span>

- 분석 중 메모리 제한 지정:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --memory-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리_제한</span>

- 분석을 위한 사용 가능한 옵션 표시:

`phpstan analyse --help`
