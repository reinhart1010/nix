---
layout: page
title: common/npm-token (English)
description: "Manage and generate authentication tokens for the npm registry."
content_hash: a2df98b53e472b7e4003591987d44f995e6555c9
last_modified_at: 2024-10-20
tldri18n_status: 2
---
# npm token

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

- Automatically configure an npm token in your global `.npmrc` file when you log in:

`npm login`

- Remove a token from the global configuration:

`npm token revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token_id</span>
