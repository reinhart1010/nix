---
layout: page
title: common/git-show-ref (한국어)
description: "Git 레퍼런스를 나열하는 명령어."
content_hash: 93c120aea1850f1780756e0283ffcf33596caff4
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-show-ref.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show-ref.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show-ref.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show-ref.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-show-ref.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git show-ref

Git 레퍼런스를 나열하는 명령어.
더 많은 정보: <https://git-scm.com/docs/git-show-ref>.

- 저장소의 모든 레퍼런스 표시:

`git show-ref`

- 헤드 레퍼런스만 표시:

`git show-ref --heads`

- 태그 레퍼런스만 표시:

`git show-ref --tags`

- 주어진 레퍼런스가 존재하는지 확인:

`git show-ref --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레퍼런스</span>
