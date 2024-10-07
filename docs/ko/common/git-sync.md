---
layout: page
title: common/git-sync (한국어)
description: "로컬 브랜치를 원격 브랜치와 동기화."
content_hash: f933d434e1d4d2cea681d1ab429f1a857fe72be8
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-sync.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-sync.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git sync

로컬 브랜치를 원격 브랜치와 동기화.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sync>.

- 현재 로컬 브랜치를 해당 원격 브랜치와 동기화:

`git sync`

- 현재 로컬 브랜치를 원격 main 브랜치와 동기화:

`git sync origin main`

- 추적되지 않은 파일을 삭제하지 않고 동기화:

`git sync -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>
