---
layout: page
title: linux/mycli (한국어)
description: "MySQL, MariaDB, Percona용 자동 완성 및 구문 강조 CLI."
content_hash: efba1a5400cce1d3c7d4659dd31dd0e38059b578
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mycli.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mycli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mycli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mycli

MySQL, MariaDB, Percona용 자동 완성 및 구문 강조 CLI.
더 많은 정보: <https://manned.org/mycli>.

- 현재 로그인된 사용자로 데이터베이스에 연결:

`mycli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 지정된 사용자로 데이터베이스에 연결:

`mycli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 지정된 호스트의 지정된 사용자로 데이터베이스에 연결:

`mycli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>
