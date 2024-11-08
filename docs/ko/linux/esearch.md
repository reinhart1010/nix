---
layout: page
title: linux/esearch (한국어)
description: "색인된 필드의 용어를 사용하여 새로운 Entrez 검색을 수행합니다."
content_hash: 12bf7fb7fb64fdb744d670902d3371c896b49122
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/esearch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/esearch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># esearch

색인된 필드의 용어를 사용하여 새로운 Entrez 검색을 수행합니다.
`edirect` 패키지의 일부입니다.
더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- pubmed 데이터베이스에서 선택적 세로토닌 재흡수 억제제를 검색:

`esearch -db pubmed -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">selective serotonin reuptake inhibitor</span>`"`

- 쿼리와 정규 표현식을 사용하여 protein 데이터베이스 검색:

`esearch -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>` -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Escherichia*'</span>

- nuccore 데이터베이스에서 메타데이터에 인슐린과 설치류가 포함된 서열 검색:

`esearch -db nuccore -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">insulin [PROT] AND rodents [ORGN]</span>`"`

- [h]도움말 표시:

`esearch -h`
