---
layout: page
title: common/gh-api (English)
description: "Makes authenticated HTTP requests to the GitHub API and prints the response."
content_hash: b6f3ea1e0db40a1ddb61c1b808707360b56c900b
---
# gh api

Makes authenticated HTTP requests to the GitHub API and prints the response.
More information: <https://cli.github.com/manual/gh_api>.

- Display the subcommand help:

`gh api --help`

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
