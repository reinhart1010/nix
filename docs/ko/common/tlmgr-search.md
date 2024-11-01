---
layout: page
title: common/tlmgr-search (한국어)
description: "(Perl) 정규 표현식을 사용하여 TeX Live 패키지를 검색."
content_hash: 7eb7059f64b21bddbd82a8eb086d342c533758af
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-search.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-search.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr search

(Perl) 정규 표현식을 사용하여 TeX Live 패키지를 검색.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 특정 정규 표현식으로 로컬에 설치된 모든 패키지의 이름 및 설명 검색:

`tlmgr search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`

- 정규 표현식으로 로컬에 설치된 모든 패키지의 파일 이름 검색:

`tlmgr search --file "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`

- 정규 표현식으로 로컬에 설치된 모든 패키지의 파일 이름, 패키지 이름 및 설명 검색:

`tlmgr search --all "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`

- 로컬 설치가 아닌 TeX Live 데이터베이스 검색:

`tlmgr search --global "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`

- 파일 이름이 아닌 패키지 이름과 설명에 대한 일치 결과를 전체 단어로 제한:

`tlmgr search --all --word "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`
