---
layout: page
title: common/git-delete-branch (한국어)
description: "로컬 및 원격 Git 브랜치 삭제."
content_hash: d86e528582a999d1b3500a7e25d3942a45159b31
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-delete-branch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-delete-branch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git delete-branch

로컬 및 원격 Git 브랜치 삭제.
`git-extras`의 일부. 체크 아웃된 브랜치를 삭제하려면 원격 브랜치만 삭제됩니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-delete-branch>.

- 하나 이상의 로컬 및 원격 Git 브랜치 삭제:

`git delete-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름1 브랜치_이름2 ...</span>
