---
layout: page
title: common/gh-auth (English)
description: "Authenticate with a GitHub host."
content_hash: 2b6439b01d3484a106bce8b60bd6d0b49ee031ca
last_modified_at: 2023-09-10
---
# gh auth

Authenticate with a GitHub host.
More information: <https://cli.github.com/manual/gh_auth>.

- Log in with interactive prompt:

`gh auth login`

- Log in with a token from `stdin` (created in <https://github.com/settings/tokens>):

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
