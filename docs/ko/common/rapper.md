---
layout: page
title: common/rapper (한국어)
description: "Raptor RDF 구문 분석 도구."
content_hash: 0e8819b881516f9322029de6891ee70cb957e865
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rapper.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rapper.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rapper

Raptor RDF 구문 분석 도구.
Raptor RDF 구문 라이브러리의 일부.
더 많은 정보: <https://librdf.org/raptor/rapper.html>.

- RDF/XML 문서를 Turtle 형식으로 변환:

`rapper -i rdfxml -o turtle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Turtle 파일의 삼중항 개수 세기:

`rapper -i turtle -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
