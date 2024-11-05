---
layout: page
title: common/nxcdb (한국어)
description: "NetExec 데이터베이스와 상호작용."
content_hash: d12b55edc956a681a5bba46f0cfa6982e6b0a3fb
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nxcdb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nxcdb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nxcdb

NetExec 데이터베이스와 상호작용.
더 많은 정보: <https://www.netexec.wiki/getting-started/database-general-usage>.

- 대화형 데이터베이스 세션 시작:

`nxcdb`

- 현재 활성화된 워크스페이스 표시:

`nxcdb --get-workspace`

- 새 워크스페이스 생성:

`nxcdb --create-workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">워크스페이스_이름</span>

- 지정된 워크스페이스 활성화:

`nxcdb --set-workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">워크스페이스_이름</span>
