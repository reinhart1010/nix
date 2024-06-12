---
layout: page
title: common/git-bisect (한국어)
description: "버그를 도입한 커밋을 찾기 위해 이진 탐색을 사용합니다."
content_hash: c4eacf9c5291a5be4389e2558db880bbcbaab9c9
last_modified_at: 2024-06-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bisect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bisect.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bisect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bisect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-bisect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git bisect

버그를 도입한 커밋을 찾기 위해 이진 탐색을 사용합니다.
Git은 자동적으로 커밋 그래프를 왔다갔다하면서 결함이 있는 커밋을 점차적으로 좁힙니다.
더 많은 정보: <https://git-scm.com/docs/git-bisect>.

- 알려진 버그가 있는 커밋과 알려진 깨끗한 (일반적으로 이전) 커밋으로 제한된 커밋 범위에서 bisect 세션 시작:

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bad_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good_commit</span>

- `git bisect`가 선택한 각 커밋에 대해 이슈를 테스트한 후 "good" 또는 "bad"로 표시:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- `git bisect`가 결함이 있는 커밋을 정확히 찾으면 bisect 세션을 종료하고 이전 브랜치로 돌아가기:

`git bisect reset`

- bisect 중 커밋 건너뛰기 (예: 다른 이슈로 인해 테스트가 실패하는 커밋):

`git bisect skip`

- 지금까지 수행된 작업에 대한 로그 표시:

`git bisect log`
