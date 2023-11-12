---
layout: page
title: common/pio-org (English)
description: "Manage PlatformIO organizations and their owners."
content_hash: ad5fb66e57a0ae45218e43d894703d4a2e0d8d5f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pio org

Manage PlatformIO organizations and their owners.
More information: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- Create a new organization:

`pio org create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>

- Delete an organization:

`pio org destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>

- Add a user to an organization:

`pio org add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user from an organization:

`pio org remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List all organizations the current user is a member of and their owners:

`pio org list`

- Update the name, email or display name of an organization:

`pio org update --orgname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_organization_name</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_email</span>` --displayname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_display_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_name</span>
