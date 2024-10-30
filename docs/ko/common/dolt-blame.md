---
layout: page
title: common/dolt-blame (한국어)
description: "Dolt 테이블의 각 행에 대한 커밋 정보를 표시."
content_hash: 851d88101a0213115cf1b193c46b0912d41cc789
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-blame.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-blame.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt blame

Dolt 테이블의 각 행에 대한 커밋 정보를 표시.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-blame>.

- 테이블의 각 행에 대한 최신 커밋을 표시:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>

- 지정된 커밋이 수행되었을 때, 테이블의 각 행에 대한 최신 커밋을 표시:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>

- 도움말 표시:

`dolt blame --help`
