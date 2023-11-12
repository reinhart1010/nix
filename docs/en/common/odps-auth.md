---
layout: page
title: common/odps-auth (English)
description: "User authorities in ODPS (Open Data Processing Service)."
content_hash: 3bb1550327aa498817a048d0342a579b77d21ff4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# odps auth

User authorities in ODPS (Open Data Processing Service).
See also `odps`.
More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Add a user to the current project:

`add user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`;`

- Grant a set of authorities to a user:

`grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_list</span>` on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_name</span>` to user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`;`

- Show authorities of a user:

`show grants for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`;`

- Create a user role:

`create role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>`;`

- Grant a set of authorities to a role:

`grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_list</span>` on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_name</span>` to role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>`;`

- Describe authorities of a role:

`desc role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>`;`

- Grant a role to a user:

`grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`;`
