---
layout: page
title: common/git-delete-squashed-branches (한국어)
description: "지정된 브랜치에 \"스쿼시 병합\"된 브랜치를 삭제하고 체크아웃합니다. 브랜치가 지정되지 않은 경우, 기본적으로 현재 체크아웃된 브랜치를 사용합니다."
content_hash: 6028295414e05d660e01a574b5bbedce03fb58f8
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-delete-squashed-branches.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git delete-squashed-branches

지정된 브랜치에 "스쿼시 병합"된 브랜치를 삭제하고 체크아웃합니다. 브랜치가 지정되지 않은 경우, 기본적으로 현재 체크아웃된 브랜치를 사용합니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-delete-squashed-branches>.

- 현재 체크아웃된 브랜치에 "스쿼시 병합"된 모든 브랜치를 삭제:

`git delete-squashed-branches`

- 특정 브랜치에 "스쿼시 병합"된 모든 브랜치를 삭제:

`git delete-squashed-branches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>
