---
layout: page
title: osx/spctl (English)
description: "Manage the security assessment policy subsystem."
content_hash: 53f245924e0c0021339356bd91434fdd7ee01158
last_modified_at: 2024-02-04
related_topics:
  - title: español version
    url: /es/osx/spctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# spctl

Manage the security assessment policy subsystem.
Utility for managing Gatekeeper in macOS.
More information: <https://keith.github.io/xcode-man-pages/spctl.8.html>.

- Turn off Gatekeeper:

`spctl --master-disable`

- Add a rule to allow an application to run (labeling of rule is optional):

`spctl --add --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Turn on Gatekeeper:

`spctl --master-enable`

- List all rules on the system:

`spctl --list`
