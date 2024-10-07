---
layout: page
title: common/git-flow (한국어)
description: "고수준 저장소 작업을 제공하는 Git 확장 모음."
content_hash: 9910643caea228c342a234f7bda347df0882666c
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-flow.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-flow.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-flow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-flow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git flow

고수준 저장소 작업을 제공하는 Git 확장 모음.
더 많은 정보: <https://github.com/nvie/gitflow>.

- 기존 Git 저장소에서 초기화:

`git flow init`

- `develop` 브랜치를 기반으로 기능 브랜치에서 개발 시작:

`git flow feature start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능</span>

- 기능 브랜치에서의 개발을 완료하고, 이를 `develop` 브랜치에 병합한 후 삭제:

`git flow feature finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능</span>

- 기능을 원격 서버에 게시:

`git flow feature publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능</span>

- 다른 사용자가 게시한 기능 가져오기:

`git flow feature pull origin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능</span>
