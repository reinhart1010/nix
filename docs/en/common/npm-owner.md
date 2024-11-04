---
layout: page
title: common/npm-owner (English)
description: "Manage ownership of published packages."
content_hash: 556add308f0f4775a45213e4eac11b7e67b21bac
last_modified_at: 2024-11-04
tldri18n_status: 2
---
# npm-owner

Manage ownership of published packages.
More information: <https://docs.npmjs.com/cli/commands/npm-owner>.

- Add a new user as a maintainer of a package:

`npm owner add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a user from a package's owner list:

`npm owner rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List all owners of a package:

`npm owner ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
