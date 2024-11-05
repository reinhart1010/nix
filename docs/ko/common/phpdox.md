---
layout: page
title: common/phpdox (한국어)
description: "PHP 문서 생성기."
content_hash: 48e32a4b1eadb6d3640c1fd40c07bb96c227ac30
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/phpdox.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/phpdox.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpdox

PHP 문서 생성기.
더 많은 정보: <https://phpdox.net>.

- 주석이 달린 스켈레톤 구성 XML 파일 표시:

`phpdox --skel`

- 현재 작업 디렉토리에 대한 문서 생성:

`phpdox`

- 특정 구성 파일을 사용하여 문서 생성:

`phpdox --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phpdox.xml</span>

- 메타데이터 수집 프로세스만 실행:

`phpdox --collector`

- 문서 생성기 프로세스만 실행:

`phpdox --generator`
