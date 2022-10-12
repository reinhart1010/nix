---
layout: page
title: common/git-clean (한국어)
description: "워킹 트리에서 추적되지 않는 파일을 제거합니다."
content_hash: 5a3e2a1d731648768fb1b5a78c55f5bf968bf132
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git clean

워킹 트리에서 추적되지 않는 파일을 제거합니다.
더 많은 정보: <https://git-scm.com/docs/git-clean>.

- 깃에 의해 추적되지 않는 파일들 지우기:

`git clean`

- 깃에 의해 추적되지 않는 파일들 인터액티브 하게 지우기:

`git clean -i`

- 어떤 파일들이 제거될 것인지 실제로 지우지 않고 보여주기:

`git clean --dry-run`

- 깃에 의해 추적되지 않는 파일들 강제적으로 지우기:

`git clean -f`

- 깃에 의해 추적되지 않는 디렉토리를 강제적으로 지우기:

`git clean -fd`

- 추적되지 않는 파일들, `.gitignore` 와 `.git/info/exclude` 안에 있는 무시된 파일들을 포함하여 지우기:

`git clean -x`
