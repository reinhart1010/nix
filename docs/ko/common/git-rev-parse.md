---
layout: page
title: common/git-rev-parse (한국어)
description: "리비전에 관련된 메타데이터를 표시."
content_hash: a3bc09586d69033e18f475d6957645f0205fd927
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-rev-parse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rev-parse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-parse.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-parse.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rev-parse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rev-parse

리비전에 관련된 메타데이터를 표시.
더 많은 정보: <https://git-scm.com/docs/git-rev-parse>.

- 브랜치의 커밋 해시 가져오기:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 현재 브랜치 이름 가져오기:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- 루트 디렉토리의 절대 경로 가져오기:

`git rev-parse --show-toplevel`
