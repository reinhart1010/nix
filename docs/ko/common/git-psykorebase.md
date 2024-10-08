---
layout: page
title: common/git-psykorebase (한국어)
description: "병합 커밋과 단 한 번의 충돌 처리를 사용하여 브랜치를 다른 브랜치 위에 리베이스합니다."
content_hash: f9f5f652bb9d4f9ba598d374e21ea7df2b231f73
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-psykorebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git psykorebase

병합 커밋과 단 한 번의 충돌 처리를 사용하여 브랜치를 다른 브랜치 위에 리베이스합니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-psykorebase>.

- 병합 커밋과 단 한 번의 충돌 처리를 사용하여 현재 브랜치를 다른 브랜치 위에 리베이스:

`git psykorebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">업스트림_브랜치</span>

- 충돌이 해결된 후 계속 진행:

`git psykorebase --continue`

- 리베이스할 브랜치 지정:

`git psykorebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">업스트림_브랜치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_브랜치</span>
