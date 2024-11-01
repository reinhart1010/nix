---
layout: page
title: common/zegrep (한국어)
description: "압축 파일에서 `egrep`을 사용하여 확장 정규 표현식 패턴 찾기."
content_hash: df9748c3759a3dafff887537000782e1ddb7140c
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zegrep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zegrep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zegrep

압축 파일에서 `egrep`을 사용하여 확장 정규 표현식 패턴 찾기.
더 많은 정보: <https://www.unix.com/man-page/freebsd/1/zegrep/>.

- 압축 파일에서 확장 정규 표현식(대소문자 구분)을 검색 (`?`, `+`, `{}`, `()` 및 `|` 지원):

`zegrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 파일에서 확장 정규 표현식(대소문자 구분 안 함)을 검색 (`?`, `+`, `{}`, `()` 및 `|` 지원):

`zegrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하지 않는 줄 검색:

`zegrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 일치하는 각 줄에 대해 파일 이름과 줄 번호 출력:

`zegrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하는 줄 검색, 일치한 텍스트만 출력:

`zegrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 파일 내의 파일을 재귀적으로 검색하여 패턴 찾기:

`zegrep --recursive "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
