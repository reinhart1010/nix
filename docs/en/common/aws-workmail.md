---
layout: page
title: common/aws-workmail (English)
description: "Manage Amazon WorkMail."
content_hash: 261e77fb2e578ca1d5fbc7e84d0f8c268965bed9
last_modified_at: 2023-07-16
---
# aws workmail

Manage Amazon WorkMail.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html>.

- List all WorkMail organizations:

`aws workmail list-organizations`

- List all users of a specific organization:

`aws workmail list-users --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_id</span>

- Create a WorkMail user in a specific organization:

`aws workmail create-user --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --display-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_id</span>

- Register and enable a group/user to WorkMail:

`aws workmail register-to-work-mail --entity-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entity_id</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_id</span>

- Create a WorkMail group in a specific organization:

`aws workmail create-group --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_id</span>

- Associate a member to a specific group:

`aws workmail associate-member-to-group --group-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>` --member-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">member_id</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_id</span>

- Deregister and disable a user/group from WorkMail:

`aws workmail deregister-from-work-mail --entity-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entity_id</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_id</span>

- Delete a user from an organization:

`aws workmail delete-user --user-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_id</span>
