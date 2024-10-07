---
layout: page
title: common/git-gc (한국어)
description: "불필요한 파일을 정리하여 로컬 저장소 최적화."
content_hash: a3934767bf65ff3b3d39932a2ad4ae7ce95034fc
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-gc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-gc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-gc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-gc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-gc.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-gc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-gc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git gc

불필요한 파일을 정리하여 로컬 저장소 최적화.
더 많은 정보: <https://git-scm.com/docs/git-gc>.

- 저장소 최적화:

`git gc`

- 더 오래 걸리지만, 강력하게 최적화:

`git gc --aggressive`

- 느슨한 객체를 제거하지 않음 (기본적으로 제거):

`git gc --no-prune`

- 모든 출력을 억제:

`git gc --quiet`

- 도움말 표시:

`git gc --help`
