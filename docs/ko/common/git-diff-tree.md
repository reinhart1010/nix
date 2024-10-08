---
layout: page
title: common/git-diff-tree (한국어)
description: "두 트리 객체를 통해 찾은 블롭의 내용과 모드를 비교."
content_hash: 40c2c78a72b717bee3d390d044387c6228d2083d
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-diff-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff-tree

두 트리 객체를 통해 찾은 블롭의 내용과 모드를 비교.
더 많은 정보: <https://git-scm.com/docs/git-diff-tree>.

- 두 트리 객체 비교:

`git diff-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish2</span>

- 특정 두 커밋 간의 변경 사항 표시:

`git diff-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit2</span>

- 패치 형식으로 변경 사항 표시:

`git diff-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--patch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish2</span>

- 특정 경로로 변경 사항 필터링:

`git diff-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish2</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
