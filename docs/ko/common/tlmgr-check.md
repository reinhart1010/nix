---
layout: page
title: common/tlmgr-check (한국어)
description: "TeX Live 설치의 일관성을 검사."
content_hash: a74a877125cace4745c60d4781c5b5ef9166bee1
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-check.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-check.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr check

TeX Live 설치의 일관성을 검사.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 전체 TeX Live 설치의 일관성을 검사:

`tlmgr check all`

- 전체 TeX Live 정보의 일관성을 자세한 모드로 검사:

`tlmgr check all -v`

- 누락된 의존성 검사:

`tlmgr check depends`

- 모든 TeX Live 실행 파일이 존재하는지 검사:

`tlmgr check executes`

- 로컬 TLPDB에 나열된 모든 파일이 존재하는지 검사:

`tlmgr check files`

- 실행 파일 섹션에서 중복된 파일 이름 검사:

`tlmgr check runfiles`
