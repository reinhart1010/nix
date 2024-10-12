---
layout: page
title: common/gh-api (한국어)
description: "GitHub API에 인증된 HTTP 요청을 보내고 응답을 출력."
content_hash: 84e9b09b238e13b8565b9f9a6a8a28142f853bf4
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-api.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh api

GitHub API에 인증된 HTTP 요청을 보내고 응답을 출력.
더 많은 정보: <https://cli.github.com/manual/gh_api>.

- 현재 저장소의 릴리스를 JSON 형식으로 표시:

`gh api repos/:owner/:repo/releases`

- 특정 이슈에 대해 반응 생성:

`gh api --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Accept:application/vnd.github.squirrel-girl-preview+json</span>` --raw-field '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content=+1</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repos/:owner/:repo/issues/123/reactions</span>

- GraphQL 쿼리 결과를 JSON 형식으로 표시:

`gh api graphql --field `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=':repo'</span>` --raw-field '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`'`

- 사용자 지정 HTTP 메서드를 사용하여 요청 전송:

`gh api --method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- HTTP 응답 헤더를 출력에 포함:

`gh api --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- 응답 본문을 출력하지 않음:

`gh api --silent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- 특정 GitHub Enterprise 서버에 요청 전송:

`gh api --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- 하위 명령 도움말 표시:

`gh api --help`
