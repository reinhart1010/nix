---
layout: page
title: linux/semanage-permissive (English)
description: "Manage persistent SELinux permissive domains."
content_hash: 14f799aba45f6a2aed3bdb94fdaaa19b22da0f2f
last_modified_at: 2024-05-27
tldri18n_status: 2
---
# semanage permissive

Manage persistent SELinux permissive domains.
Note that this effectively makes the process unconfined. For long-term use, it is recommended to configure SELiunx properly.
See also: `semanage`, `getenforce`, `setenforce`.
More information: <https://manned.org/man/semanage-permissive>.

- List all process types (a.k.a domains) that are in permissive mode:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- Set or unset permissive mode for a domain:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add|-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_t</span>
