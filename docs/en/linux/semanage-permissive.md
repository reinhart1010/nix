---
layout: page
title: linux/semanage-permissive (English)
description: "Manage persistent SELinux permissive domains."
content_hash: 58630fa1de07837aafd2239cc326d1d6d531f0e2
last_modified_at: 2024-09-19
related_topics:
  - title: Nederlands version
    url: /nl/linux/semanage-permissive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# semanage permissive

Manage persistent SELinux permissive domains.
Note that this effectively makes the process unconfined. For long-term use, it is recommended to configure SELiunx properly.
See also: `semanage`, `getenforce`, `setenforce`.
More information: <https://manned.org/semanage-permissive>.

- List all process types (a.k.a domains) that are in permissive mode:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- Set or unset permissive mode for a domain:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add|-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_t</span>
