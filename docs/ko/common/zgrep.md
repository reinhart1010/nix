---
layout: page
title: common/zgrep (한국어)
description: "압축 파일 내에서 텍스트 패턴을 검색하는 도구 (`grep -Z`와 동등)."
content_hash: c023bd3df84b4ba16878b9fc632b05b0d1555ab4
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zgrep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zgrep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zgrep

압축 파일 내에서 텍스트 패턴을 검색하는 도구 (`grep -Z`와 동등).
더 많은 정보: <https://manned.org/zgrep>.

- 압축 파일에서 패턴 검색 (대소문자 구분):

`zgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축/파일</span>

- 압축 파일에서 패턴 검색 (대소문자 구분 안 함):

`zgrep -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축/파일</span>

- 일치하는 패턴이 포함된 행의 개수를 출력:

`zgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축/파일</span>

- 패턴이 없는 행을 표시 (검색 기능 반전):

`zgrep -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축/파일</span>

- 여러 패턴으로 압축 파일 검색:

`zgrep -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴_1</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴_2</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축/파일</span>

- 확장 정규 표현식 사용 (`?`, `+`, `{}`, `()` 및 `|` 지원):

`zgrep -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 일치 항목 전후로 3줄의 [C]ontext, [B]efore, 또는 [A]fter 출력:

`zgrep -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C|B|A</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축/파일</span>
