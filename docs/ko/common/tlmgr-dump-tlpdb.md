---
layout: page
title: common/tlmgr-dump-tlpdb (한국어)
description: "TeX Live 패키지 데이터베이스 덤프."
content_hash: 2f41f16bf82b1cd73d8db6056ddc513781f6b296
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-dump-tlpdb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-dump-tlpdb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr dump-tlpdb

TeX Live 패키지 데이터베이스 덤프.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 로컬 패키지 데이터베이스 덤프:

`tlmgr dump-tlpdb --local`

- 원격 패키지 데이터베이스 덤프:

`tlmgr dump-tlpdb --remote`

- 로컬 패키지 데이터베이스를 JSON 형식으로 덤프:

`tlmgr dump-tlpdb --local --json`
