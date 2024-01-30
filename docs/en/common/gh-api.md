---
layout: page
title: common/gh-api (English)
description: "Makes authenticated HTTP requests to the GitHub API and prints the response."
content_hash: dce73bd356ffc8f9f9d9208f84214f6eace66f21
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# gh api

Makes authenticated HTTP requests to the GitHub API and prints the response.
More information: <https://cli.github.com/manual/gh_api>.

- Display the releases for the current repository in JSON format:

`gh api repos/:owner/:repo/releases`

- Create a reaction for a specific issue:

`gh api --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Accept:application/vnd.github.squirrel-girl-preview+json</span>` --raw-field '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content=+1</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repos/:owner/:repo/issues/123/reactions</span>

- Display the result of a GraphQL query in JSON format:

`gh api graphql --field `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=':repo'</span>` --raw-field '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`'`

- Send a request using a custom HTTP method:

`gh api --method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- Include the HTTP response headers in the output:

`gh api --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- Do not print the response body:

`gh api --silent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- Send a request to a specific GitHub Enterprise Server:

`gh api --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>

- Display the subcommand help:

`gh api --help`
