---
layout: page
title: common/highlight (한국어)
description: "구문 강조된 소스 코드를 다양한 형식으로 출력."
content_hash: 3cadfda0d70177be44701c6c09a001afb52c6540
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/highlight.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/highlight.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># highlight

구문 강조된 소스 코드를 다양한 형식으로 출력.
더 많은 정보: <http://www.andre-simon.de/doku/highlight/highlight.php>.

- 소스 코드 파일에서 완전한 HTML 문서를 생성:

`highlight --out-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테마_이름</span>` --syntax `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_코드</span>

- 더 큰 문서에 포함하기에 적합한 HTML 조각을 생성:

`highlight --out-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` --fragment --syntax `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일</span>

- 모든 태그에 CSS 스타일을 인라인:

`highlight --out-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` --inline-css --syntax `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일</span>

- 지원되는 모든 언어, 테마 또는 플러그인을 나열:

`highlight --list-scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">langs|themes|plugins</span>

- 테마에 대한 CSS 스타일시트를 출력:

`highlight --out-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` --print-style --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테마_이름</span>` --syntax `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>`] --stdout`
