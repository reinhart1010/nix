---
layout: page
title: common/npm-login (English)
description: "Login to a registry user account."
content_hash: eddd0e6d7d08d0da8f9b709fe6b4cb2ac822c155
last_modified_at: 2024-11-11
tldri18n_status: 2
---
# npm login

Login to a registry user account.
More information: <https://docs.npmjs.com/cli/commands/npm-login>.

- Login to a registry user account and save the credentials to the `.npmrc` file:

`npm login`

- Login, using a custom registry:

`npm login --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_url</span>

- Login, using a specific authentication strategy:

`npm login --auth-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacy|web</span>
