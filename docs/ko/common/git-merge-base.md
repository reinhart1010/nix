---
layout: page
title: common/git-merge-base (한국어)
description: "두 커밋의 공통 조상을 찾습니다."
content_hash: 24536bf9e6ae977ab1d5b80bd3fd15e2ead2ab0b
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-merge-base.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git merge-base

두 커밋의 공통 조상을 찾습니다.
더 많은 정보: <https://git-scm.com/docs/git-merge-base>.

- 두 커밋의 최상의 공통 조상을 출력:

`git merge-base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- 두 커밋의 모든 최상의 공통 조상을 출력:

`git merge-base --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- 특정 커밋이 다른 커밋의 조상인지 확인:

`git merge-base --is-ancestor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancestor_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
