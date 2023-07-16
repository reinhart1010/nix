---
layout: page
title: common/gh-auth (English)
description: "Authenticate with a GitHub host."
content_hash: 3df5bf947c77335dedde0897c20ebca1565acf77
last_modified_at: 2023-07-16
---
# gh auth

Authenticate with a GitHub host.
More information: <https://cli.github.com/manual/gh_auth>.

- Log in with interactive prompt:

`gh auth login`

- Log in with a token from standard input (created in https://github.com/settings/tokens):

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_token</span>` | gh auth login --with-token`

- Check if you are logged in:

`gh auth status`

- Log out:

`gh auth logout`

- Log in with a specific GitHub Enterprise Server:

`gh auth login --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.example.com</span>

- Refresh the session to ensure authentication credentials have the correct minimum scopes (removes additional scopes requested previously):

`gh auth refresh`

- Expand the permission scopes:

`gh auth refresh --scopes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...</span>
