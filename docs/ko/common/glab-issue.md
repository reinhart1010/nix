---
layout: page
title: common/glab-issue (한국어)
description: "GitLab 이슈 관리."
content_hash: e659147278ce5b11cc845cd26f79b56acfe414de
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/glab-issue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glab issue

GitLab 이슈 관리.
더 많은 정보: <https://glab.readthedocs.io/en/latest/issue>.

- 특정 이슈 표시:

`glab issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>

- 기본 웹 브라우저에 특정 문제를 표시:

`glab issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>` --web`

- 기본 웹 브라우저에 새로운 이슈를 생성:

`glab issue create --web`

- `bug` 라벨이 있는 최근 10개 문제를 나열:

`glab issue list --per-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- 특정 사용자가 작성한 닫힌 이슈를 나열:

`glab issue list --closed --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 이슈 다시 열기:

`glab issue reopen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>
