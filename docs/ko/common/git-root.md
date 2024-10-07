---
layout: page
title: common/git-root (한국어)
description: "현재 Git 저장소의 루트 디렉토리를 출력."
content_hash: f223ac0c671fbff0cdc77f27cc892b98c0727ffe
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-root.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-root.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git root

현재 Git 저장소의 루트 디렉토리를 출력.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-root>.

- 현재 Git 저장소의 절대 경로 출력:

`git root`

- 현재 작업 디렉토리를 현재 Git 저장소의 루트에 상대적으로 출력:

`git root --relative`
