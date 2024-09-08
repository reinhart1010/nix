---
layout: page
title: linux/audit2allow (English)
description: "Create an SELinux local policy module to allow rules based on denied operations found in logs."
content_hash: 64b14ebb714a4ef4fa744be258cb6aa888bf789c
last_modified_at: 2024-09-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/audit2allow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># audit2allow

Create an SELinux local policy module to allow rules based on denied operations found in logs.
Note: Use audit2allow with caution—always review the generated policy before applying it, as it may allow excessive access.
More information: <https://manned.org/audit2allow>.

- Generate a local policy to allow access for all denied services:

`sudo audit2allow --all -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>

- Generate a local policy module to grant access to a specific process/service/command from the audit logs:

`sudo grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache2</span>` /var/log/audit/audit.log | sudo audit2allow -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>

- Inspect and review the Type Enforcement (.te) file for a local policy:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>`.te`

- Install a local policy module:

`sudo semodule -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>`.pp`
