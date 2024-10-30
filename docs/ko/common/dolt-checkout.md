---
layout: page
title: common/dolt-checkout (한국어)
description: "작업 트리나 테이블을 브랜치나 커밋으로 체크아웃."
content_hash: 93daf38c0ce24531f71279c1799d6fb9ab4ea525
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-checkout.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-checkout.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt checkout

작업 트리나 테이블을 브랜치나 커밋으로 체크아웃.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-checkout>.

- 브랜치 교체:

`dolt checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 스테이지되지 않은 변경 사항을 테이블로 되돌림:

`dolt checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>

- 새로운 브랜치를 생성하고, 그 브랜치로 체크아웃:

`dolt checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 지정된 커밋을 기반으로 새로운 브랜치를 생성하고 해당 커밋으로 전환:

`dolt checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>
