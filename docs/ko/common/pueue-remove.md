---
layout: page
title: common/pueue-remove (한국어)
description: "작업 목록에서 작업 제거. 실행 중이거나 일시 중지된 작업은 먼저 종료되어야 합니다."
content_hash: 0b519b09e0bad4cb9a7bd34537e6b7a388e6f101
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-remove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-remove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue remove

작업 목록에서 작업 제거. 실행 중이거나 일시 중지된 작업은 먼저 종료되어야 합니다.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 종료되거나 완료된 작업 제거:

`pueue remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 여러 작업을 한 번에 제거:

`pueue remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>
