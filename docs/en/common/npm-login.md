---
layout: page
title: common/npm-login (English)
description: "Login to a registry user account."
content_hash: 2a9d8508e4cb42670ca821b7d4a3518b2bfb87ea
last_modified_at: 2024-11-16
tldri18n_status: 2
---
# npm login

Login to a registry user account.
See also: `npm logout` for logging out.
More information: <https://docs.npmjs.com/cli/commands/npm-login>.

- Login to a registry user account and save the credentials to the `.npmrc` file:

`npm login`

- Login using a custom registry:

`npm login --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_url</span>

- Login using a specific authentication strategy:

`npm login --auth-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacy|web</span>
