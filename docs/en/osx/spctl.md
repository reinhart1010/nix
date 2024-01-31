---
layout: page
title: osx/spctl (English)
description: "Manage the security assessment policy subsystem."
content_hash: ea3c86c88338cb4511291ace4a86bbf210cb2f73
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/spctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# spctl

Manage the security assessment policy subsystem.
Utility for managing Gatekeeper in macOS.
More information: <https://keith.github.io/xcode-man-pages/SPCTL.8.html>.

- Turn off Gatekeeper:

`spctl --master-disable`

- Add a rule to allow an application to run (labeling of rule is optional):

`spctl --add --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Turn on Gatekeeper:

`spctl --master-enable`

- List all rules on the system:

`spctl --list`
