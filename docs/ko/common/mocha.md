---
layout: page
title: common/mocha (한국어)
description: "기능이 풍부한 JavaScript 테스트 프레임워크."
content_hash: 4799b9d7a61a796ed71b6be4333c9b08ae3bdc11
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mocha.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mocha.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mocha

기능이 풍부한 JavaScript 테스트 프레임워크.
더 많은 정보: <https://mochajs.org>.

- 기본 설정 또는 `mocha.opts`에 구성된 대로 테스트 실행:

`mocha`

- 특정 위치에 포함된 테스트 실행:

`mocha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트가_있는_디렉토리</span>

- 특정 `grep` 패턴과 일치하는 테스트 실행:

`mocha --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 현재 디렉토리의 JavaScript 파일 변경 시 및 최초 실행 시 테스트 실행:

`mocha --watch`

- 특정 리포터로 테스트 실행:

`mocha --reporter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리포터</span>
