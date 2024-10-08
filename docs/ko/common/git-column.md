---
layout: page
title: common/git-column (한국어)
description: "데이터를 여러 열로 표시."
content_hash: 6a4a5eca013930d8eacfa61dbf9495553f2476dd
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-column.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-column.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-column.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git column

데이터를 여러 열로 표시.
더 많은 정보: <https://git-scm.com/docs/git-column>.

- `stdin`을 여러 열로 형식화:

`ls | git column --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>

- 최대 너비가 `100`인 여러 열로 `stdin`을 형식화:

`ls | git column --mode=column --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- 최대 여백이 `30`인 여러 열로 `stdin`을 형식화:

`ls | git column --mode=column --padding=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
