---
layout: page
title: common/pint (한국어)
description: "PHP 코드 스타일을 고정하는 의견이 반영된 도구로, PHP-CS-Fixer를 기반으로 합니다."
content_hash: 42b685fac14abe10acc06857089d651751d923d9
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Pint

PHP 코드 스타일을 고정하는 의견이 반영된 도구로, PHP-CS-Fixer를 기반으로 합니다.
더 많은 정보: <https://laravel.com/docs/pint>.

- 코드 스타일 수정 실행:

`pint`

- 변경된 모든 파일 표시:

`pint -v`

- 변경을 적용하지 않고 코드 스타일 린팅 실행:

`pint --test`

- 특정 구성 파일을 사용하여 코드 스타일 수정 실행:

`pint --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pint.json</span>

- 특정 프리셋을 사용하여 코드 스타일 수정 실행:

`pint --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psr12</span>
