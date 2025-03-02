---
layout: page
title: linux/audit2allow (English)
description: "Create an SELinux local policy module to allow rules based on denied operations found in logs."
content_hash: 7eff63e0e2b3f87283ba6c942db80d7497d42976
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/audit2allow.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/audit2allow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# audit2allow

Create an SELinux local policy module to allow rules based on denied operations found in logs.
Note: Use audit2allow with caution. Always review the generated policy before applying it, as it may allow excessive access.
More information: <https://manned.org/audit2allow>.

- Generate a local policy to allow access for all denied services:

`sudo audit2allow --all -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>

- Generate a local policy module to grant access to a specific process/service/command from the audit logs:

`sudo grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache2</span>` /var/log/audit/audit.log | sudo audit2allow -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>

- Inspect and review the Type Enforcement (.te) file for a local policy:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>`.te`

- Install a local policy module:

`sudo semodule -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_policy_name</span>`.pp`
