---
layout: page
title: common/perldoc (한국어)
description: "`.pod` 형식의 Perl 문서를 조회."
content_hash: aeaad3825ebeb302e101236845047c68aa02d9a1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/perldoc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/perldoc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># perldoc

`.pod` 형식의 Perl 문서를 조회.
더 많은 정보: <https://perldoc.perl.org/perldoc>.

- 내장 함수, 변수 또는 API에 대한 문서 보기:

`perldoc -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f|v|a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- Perl FAQ의 질문 제목에서 검색:

`perldoc -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규식</span>

- 출력을 직접 `stdout`으로 전송 (기본적으로 페이저로 전송됨):

`perldoc -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지|모듈|프로그램|URL</span>

- 원하는 번역의 언어 코드를 지정:

`perldoc -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어_코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지|모듈|프로그램|URL</span>
