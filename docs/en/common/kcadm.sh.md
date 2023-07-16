---
layout: page
title: common/kcadm.sh (English)
description: "Perform administration tasks."
content_hash: c0405b67b3720dd24fbba39479ac621c9d37a58d
last_modified_at: 2023-07-16
---
# kcadm.sh

Perform administration tasks.
More information: <https://www.keycloak.org/docs/latest/server_admin/#admin-cli>.

- Start an authenticated session:

`kcadm.sh config credentials --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --realm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">realm_name</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Create a user:

`kcadm.sh create users -s username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">realm_name</span>

- List all realms:

`kcadm.sh get realms`

- Update a realm with JSON config:

`kcadm.sh update realms/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">realm_name</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>
