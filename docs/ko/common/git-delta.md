---
layout: page
title: common/git-delta (한국어)
description: "다른 브랜치와 다른 파일을 나열."
content_hash: 91fade2c5892fba1df418ef84979ed3b2356f95f
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-delta.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git delta

다른 브랜치와 다른 파일을 나열.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-delta>.

- 현재 체크아웃된 브랜치와 `main` 브랜치가 다른 파일을 나열:

`git delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main</span>

- 특정 브랜치와 다른 특정 브랜치가 다른 파일을 나열:

`git delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_2</span>
