---
layout: page
title: common/gh-alias (한국어)
description: "GitHub CLI 명령 별칭 관리."
content_hash: a701f3306e45a581d83f3b1557c217a22911f176
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-alias.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gh-alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh alias

GitHub CLI 명령 별칭 관리.
더 많은 정보: <https://cli.github.com/manual/gh_alias>.

- `gh`에 설정된 모든 별칭 나열:

`gh alias list`

- `gh` 하위 명령 별칭 생성:

`gh alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pv</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr view</span>`'`

- 셸 명령을 `gh` 하위 명령으로 설정:

`gh alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 명령 단축키 삭제:

`gh alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭_이름</span>

- 하위 명령 도움말 표시:

`gh alias`
