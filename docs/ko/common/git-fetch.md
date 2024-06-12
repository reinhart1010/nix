---
layout: page
title: common/git-fetch (한국어)
description: "원격 저장소에서 객체와 참조를 다운로드합니다."
content_hash: 30645dcf4becad191e34db6ab7221ab1d804f302
last_modified_at: 2024-06-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-fetch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-fetch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-fetch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-fetch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fetch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-fetch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git fetch

원격 저장소에서 객체와 참조를 다운로드합니다.
더 많은 정보: <https://git-scm.com/docs/git-fetch>.

- 기본 원격 업스트림 저장소로부터 최신 변경 사항 가져오기 (설정된 경우):

`git fetch`

- 특정 원격 업스트림 저장소에서 새 브랜치 가져오기:

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- 모든 원격 업스트림 저장소에서 최신 변경 사항 가져오기:

`git fetch --all`

- 원격 업스트림 저장소에서 태그도 함께 가져오기:

`git fetch --tags`

- 업스트림에서 삭제된 원격 브랜치에 대한 로컬 참조 삭제:

`git fetch --prune`
