---
layout: page
title: common/git-revert (한국어)
description: "이전 커밋의 영향을 되돌리는 새로운 커밋을 생성합니다."
content_hash: 414dbe68c82882347cfd5c8e833a3f14d637f4b6
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-revert.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-revert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-revert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-revert.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-revert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git revert

이전 커밋의 영향을 되돌리는 새로운 커밋을 생성합니다.
더 많은 정보: <https://git-scm.com/docs/git-revert>.

- 가장 최근 커밋 되돌리기:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- 마지막에서 5번째 커밋 되돌리기:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 특정 커밋 되돌리기:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9</span>

- 여러 커밋 되돌리기:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name~5..branch_name~2</span>

- 새로운 커밋을 생성하지 않고 작업 트리만 변경:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--no-commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
