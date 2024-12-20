---
layout: page
title: common/npm-cache (English)
description: "Manage the npm package cache."
content_hash: e557bbf61bcf463096a73a2dbb5c069008f599f5
last_modified_at: 2024-10-28
tldri18n_status: 2
---
# npm cache

Manage the npm package cache.
More information: <https://docs.npmjs.com/cli/commands/npm-cache>.

- Add a specific package to the cache:

`npm cache add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a specific package from the cache:

`npm cache remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Clear a specific cached item by key:

`npm cache clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Clear the entire npm cache:

`npm cache clean --force`

- List the contents of the npm cache:

`npm cache ls`

- Verify the integrity of the npm cache:

`npm cache verify`

- Show information about the npm cache location and configuration:

`npm cache dir`

- Change the cache path:

`npm config set cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
