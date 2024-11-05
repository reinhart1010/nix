---
layout: page
title: common/php-cs-fixer (한국어)
description: "PHP 코딩 스타일 자동 수정 도구."
content_hash: a5f707d07587690fd63ed4aadcbdd021b3b937ff
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/php-cs-fixer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/php-cs-fixer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># PHP-CS-Fixer

PHP 코딩 스타일 자동 수정 도구.
더 많은 정보: <https://github.com/FriendsOfPHP/PHP-CS-Fixer>.

- 현재 디렉토리에서 코드 스타일 수정 실행:

`php-cs-fixer fix`

- 특정 디렉토리에서 코드 스타일 수정 실행:

`php-cs-fixer fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 변경 사항을 적용하지 않고 코드 스타일 검사 실행:

`php-cs-fixer fix --dry-run`

- 특정 규칙을 사용하여 코드 스타일 수정 실행:

`php-cs-fixer fix --rules=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙들</span>

- 적용된 규칙 표시:

`php-cs-fixer fix --verbose`

- 다른 형식으로 결과 출력:

`php-cs-fixer fix --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt|json|xml|checkstyle|junit|gitlab</span>

- 수정이 필요한 파일 표시:

`php-cs-fixer list-files`

- 규칙 또는 규칙 세트 설명:

`php-cs-fixer describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙</span>
