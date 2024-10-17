---
layout: page
title: common/npm-token (English)
description: "Manage and generate authentication tokens for the npm registry."
content_hash: 6d9264bfba4d69f35b1f80242d1faaf6be0f5cde
last_modified_at: 2024-10-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-token.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm token

Manage and generate authentication tokens for the npm registry.
More information: <https://docs.npmjs.com/cli/commands/npm-token>.

- Create a new authentication token:

`npm token create`

- List all tokens associated with an account:

`npm token list`

- Delete a specific token using its token ID:

`npm token revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token_id</span>

- Create a token with read-only access:

`npm token create --read-only`

- Create a token with publish access:

`npm token create --publish`

- Automatically configure an npm token in your global .npmrc file when you log in:

`npm login`

- Remove a token from the global configuration:

`npm token revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token_id</span>
