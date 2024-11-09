---
layout: page
title: common/tb (한국어)
description: "여러 보드에서 작업과 메모를 관리."
content_hash: bb2fe540f2850f600d2393fe69ffa9750f85a7d0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tb

여러 보드에서 작업과 메모를 관리.
더 많은 정보: <https://github.com/klaussinani/taskbook>.

- 보드에 새 작업 추가:

`tb --task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_설명</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">보드_이름</span>

- 보드에 새 메모 추가:

`tb --note `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모_설명</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">보드_이름</span>

- 항목의 우선순위 수정:

`tb --priority @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>

- 항목 체크/체크 해제:

`tb --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_ID</span>

- 체크된 모든 항목 아카이브:

`tb --clear`

- 항목을 다른 보드로 이동:

`tb --move @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">보드_이름</span>
