---
layout: page
title: common/tlmgr-backup (한국어)
description: "TeX Live 패키지의 백업을 관리."
content_hash: 454d1d381d790cdc71b45c9486c98f7ebf6a4a11
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-backup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-backup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr backup

TeX Live 패키지의 백업을 관리.
기본 백업 디렉토리는 `backupdir` 옵션에 의해 지정되며, `tlmgr option`으로 확인 가능.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 하나 이상의 패키지 백업:

`tlmgr backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 모든 패키지 백업:

`tlmgr backup --all`

- 사용자 지정 디렉토리에 백업:

`tlmgr backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --backupdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업_디렉토리</span>

- 하나 이상의 패키지 백업 삭제:

`tlmgr backup clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 모든 백업 삭제:

`tlmgr backup clean --all`
