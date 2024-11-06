---
layout: page
title: common/hg-update (한국어)
description: "작업 디렉터리를 지정된 변경 집합으로 업데이트."
content_hash: bc303897e1068cef59edd199e68f836d6bc5a55d
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hg-update.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hg-update.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hg update

작업 디렉터리를 지정된 변경 집합으로 업데이트.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#update>.

- 현재 브랜치의 최신 변경 사항으로 업데이트:

`hg update`

- 지정된 리비전으로 업데이트:

`hg update --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>

- 커밋되지 않은 변경 사항을 폐기하고 업데이트:

`hg update --clean`

- 지정된 날짜와 일치하는 마지막 커밋으로 업데이트:

`hg update --date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일-월-연도</span>
