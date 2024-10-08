---
layout: page
title: common/git-graft (한국어)
description: "브랜치의 커밋들을 다른 브랜치로 병합하고, 소스 브랜치를 삭제."
content_hash: b59ee6979ff50ec59a120aec2af74152747d0292
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-graft.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git graft

브랜치의 커밋들을 다른 브랜치로 병합하고, 소스 브랜치를 삭제.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-graft>.

- 소스 브랜치의 모든 커밋을 대상 브랜치로 병합하고, 소스 브랜치를 삭제:

`git graft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_branch</span>
