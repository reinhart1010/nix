---
layout: page
title: common/pio-access (English)
description: "Set the access level on published resources (packages) in the registry."
content_hash: 5eb40a66156055cce69f49211e9ae25cf62d4091
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pio access

Set the access level on published resources (packages) in the registry.
More information: <https://docs.platformio.org/en/latest/core/userguide/access/>.

- Grant a user access to a resource:

`pio access grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest|maintainer|admin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_urn</span>

- Remove a user's access to a resource:

`pio access revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_urn</span>

- Show all resources that a user or team has access to and the access level:

`pio access list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Restrict access to a resource to specific users or team members:

`pio access private `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_urn</span>

- Allow all users access to a resource:

`pio access public `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_urn</span>
