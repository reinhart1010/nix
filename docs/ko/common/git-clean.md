---
layout: page
title: common/git-clean (한국어)
description: "워킹 트리에서 추적되지 않는 파일을 제거합니다."
content_hash: ca3c52f4d0e70bb690e26260dfecd1f1e9ee4ecf
last_modified_at: 2024-10-07
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
  - title: Indonesia version
    url: /id/common/git-clean.html
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
tldri18n_status: 2
---
# git clean

워킹 트리에서 추적되지 않는 파일을 제거합니다.
더 많은 정보: <https://git-scm.com/docs/git-clean>.

- 깃에 의해 추적되지 않는 파일들 지우기:

`git clean`

- 깃에 의해 추적되지 않는 파일들 인터액티브 하게 지우기:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>

- 어떤 파일들이 제거될 것인지 실제로 지우지 않고 보여주기:

`git clean --dry-run`

- 깃에 의해 추적되지 않는 파일들 강제적으로 지우기:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- 추적되지 않은 [d]irectory 강제로 삭제:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` -d`

- 추적되지 않는 파일들, `.gitignore` 와 `.git/info/exclude` 안에 있는 무시된 파일들을 포함하여 지우기:

`git clean -x`
