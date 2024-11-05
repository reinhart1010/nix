---
layout: page
title: common/hub-issue (한국어)
description: "Github 이슈를 관리."
content_hash: cf256283cebfa853af497ad9d1c8b84d32aeb11f
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/hub-issue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hub issue

Github 이슈를 관리.
더 많은 정보: <https://hub.github.com/hub-issue.1.html>.

- `bug` 라벨이 있는 최근 10개 문제를 나열:

`hub issue list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --labels "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- 특정 문제를 표시:

`hub issue show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>

- 특정 사용자에게 할당된 10개의 종결된 문제를 나열:

`hub issue --state `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">closed</span>` --assignee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
