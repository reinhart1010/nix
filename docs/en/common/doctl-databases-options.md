---
layout: page
title: common/doctl-databases-options (English)
description: "Enable the navigation of available options under each database engine."
content_hash: 362037a6a8faea0ae056c93cf4abe9fe41c7a173
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# doctl databases options

Enable the navigation of available options under each database engine.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/options>.

- Run a `doctl databases options` command with an access token:

`doctl databases options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Retrieve a list of the available database engines:

`doctl databases options engines`

- Retrieve a list of the available regions for a given database engine:

`doctl databases options regions --engine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pg|mysql|redis|mongodb</span>

- Retrieve a list of the available slugs for a given database engine:

`doctl databases options slugs --engine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pg|mysql|redis|mongodb</span>

- Retrieve a list of the available versions for a given database engine:

`doctl databases options versions --engine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pg|mysql|redis|mongodb</span>
