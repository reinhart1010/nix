---
layout: page
title: common/glab-alias (한국어)
description: "GitLab CLI 명령어 별칭을 관리."
content_hash: df8c7030f36e8fb2e17cf574a2eb1ec2ba18103c
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/glab-alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glab alias

GitLab CLI 명령어 별칭을 관리.
더 많은 정보: <https://glab.readthedocs.io/en/latest/alias>.

- 하위 명령어 도움말을 표시:

`glab alias`

- `glab`이 사용하도록 구성된 모든 별칭을 나열:

`glab alias list`

- `glab` 하위 명령 별칭을 생성:

`glab alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mrv</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr view</span>`'`

- 쉘 명령을 `glab` 하위 명령으로 설정:

`glab alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령 단축키 삭제:

`glab alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_이름</span>
