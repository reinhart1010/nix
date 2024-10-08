---
layout: page
title: common/git-summary (한국어)
description: "Git 저장소에 대한 정보를 표시."
content_hash: 82c3976ccbdee5cce6a9b901507ac4eed25ae80a
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-summary.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git summary

Git 저장소에 대한 정보를 표시.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>.

- Git 저장소에 대한 정보 표시:

`git summary`

- 특정 커밋 이후의 Git 저장소에 대한 정보 표시:

`git summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋|브랜치_명|태그_명</span>

- 서로 다른 이메일을 사용하는 커미터를 저자별 통계로 합산하여 Git 저장소에 대한 정보 표시:

`git summary --dedup-by-email`

- 각 기여자가 수정한 줄 수를 표시하여 Git 저장소에 대한 정보 표시:

`git summary --line`
