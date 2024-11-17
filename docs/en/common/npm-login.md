---
layout: page
title: common/npm-login (English)
description: "Log in to a registry user account."
content_hash: 6488ef61d73ea1d39663b04d36ee20252714d18f
last_modified_at: 2024-11-17
tldri18n_status: 2
---
# npm login

Log in to a registry user account.
See also: `npm logout` for logging out.
More information: <https://docs.npmjs.com/cli/commands/npm-login>.

- Log in to a registry user account and save the credentials to the `.npmrc` file:

`npm login`

- Log in using a custom registry:

`npm login --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_url</span>

- Log in using a specific authentication strategy:

`npm login --auth-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacy|web</span>
