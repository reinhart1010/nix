---
layout: page
title: common/npm-org (English)
description: "Manage organizations."
content_hash: 673bfde451f0518680c42fb4c456655689e1132b
last_modified_at: 2024-11-16
related_topics:
  - title: 한국어 version
    url: /ko/common/npm-org.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm org

Manage organizations.
More information: <https://docs.npmjs.com/cli/commands/npm-org>.

- Add a new user to an organization:

`npm org set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Change a user's role in an organization:

`npm org set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">developer|admin|owner</span>

- Remove a user from an organization:

`npm org rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List all users in an organization:

`npm org ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>

- List all users in an organization, output in JSON format:

`npm org ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>` --json`

- Display a user's role in an organization:

`npm org ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
