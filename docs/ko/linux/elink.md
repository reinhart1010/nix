---
layout: page
title: linux/elink (한국어)
description: "데이터베이스 내에서 미리 계산된 이웃을 조회하거나 다른 데이터베이스에서 관련 레코드를 찾습니다."
content_hash: cdb9d8ec1eb7ba56611e1a03f8cb9e6ea38d3166
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/elink.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/elink.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># elink

데이터베이스 내에서 미리 계산된 이웃을 조회하거나 다른 데이터베이스에서 관련 레코드를 찾습니다.
`edirect` 패키지의 일부입니다.
더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- pubmed를 검색한 후 관련 시퀀스 찾기:

`esearch -db pubmed -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택적 세로토닌 재흡수 억제제</span>`" | elink -target nuccore`

- 뉴클레오타이드를 검색한 후 관련 생물 샘플 찾기:

`esearch -db nuccore -query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인슐린 [PROT] AND 설치류 [ORGN]</span>`" | elink -target biosample`
