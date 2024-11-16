---
layout: page
title: common/npm-owner (English)
description: "Manage ownership of published packages."
content_hash: 0a6815c60588cc0270a995c716159b4bd0a175e4
last_modified_at: 2024-11-16
related_topics:
  - title: 한국어 version
    url: /ko/common/npm-owner.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm owner

Manage ownership of published packages.
More information: <https://docs.npmjs.com/cli/commands/npm-owner>.

- Add a new user as a maintainer of a package:

`npm owner add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a user from a package's owner list:

`npm owner rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List all owners of a package:

`npm owner ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
