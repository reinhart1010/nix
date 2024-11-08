---
layout: page
title: linux/einfo (한국어)
description: "각 데이터베이스 필드에 색인된 레코드 수, 데이터베이스의 마지막 업데이트 날짜 및 데이터베이스에서 다른 Entrez 데이터베이스로의 사용 가능한 링크를 제공합니다."
content_hash: 010f85f0cd4e2d60b098baf9c6a11a00d6df42c3
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/einfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/einfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># einfo

각 데이터베이스 필드에 색인된 레코드 수, 데이터베이스의 마지막 업데이트 날짜 및 데이터베이스에서 다른 Entrez 데이터베이스로의 사용 가능한 링크를 제공합니다.
더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- 모든 데이터베이스 이름 출력:

`einfo -dbs`

- 단백질 데이터베이스의 모든 정보를 XML 형식으로 출력:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>

- nuccore 데이터베이스의 모든 필드 출력:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuccore</span>` -fields`

- 단백질 데이터베이스의 모든 링크 출력:

`einfo -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protein</span>` -links`
