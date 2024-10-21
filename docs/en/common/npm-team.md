---
layout: page
title: common/npm-team (English)
description: "Manage teams in an organization on the `npm` registry."
content_hash: 77a27a9633dcfe60a04131a30d9f6c0ac0fcd63e
last_modified_at: 2024-10-21
tldri18n_status: 2
---
# npm team

Manage teams in an organization on the `npm` registry.
More information: <https://docs.npmjs.com/cli/commands/npm-team>.

- Add a user to a team in an organization:

`npm team add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization:team</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user from a team:

`npm team rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization:team</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a new team in an organization:

`npm team create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization:team</span>

- Delete a team from an organization:

`npm team destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization:team</span>

- List all teams in an organization:

`npm team ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- List all users in a specific team:

`npm team ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization:team</span>
