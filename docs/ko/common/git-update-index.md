---
layout: page
title: common/git-update-index (한국어)
description: "Git 색인을 조작하기 위한 명령어."
content_hash: e2a735e62e1d7131341e228bae542657f5fa6cd2
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-update-index.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-update-index.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-update-index.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git update-index

Git 색인을 조작하기 위한 명령어.
더 많은 정보: <https://git-scm.com/docs/git-update-index>.

- 수정된 파일이 변경되지 않은 것처럼 가장하기 (`git status`에서 변경 사항으로 표시되지 않음):

`git update-index --skip-worktree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/수정된_파일</span>
