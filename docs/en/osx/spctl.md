---
layout: page
title: osx/spctl (English)
description: "Manage the security assessment policy subsystem."
content_hash: c96018fdef699274d14bf6defd3c303eb17d7531
---
# spctl

Manage the security assessment policy subsystem.
Utility for managing Gatekeeper in macOS.
More information: <https://www.unix.com/man-page/osx/8/SPCTL/>.

- Turn off Gatekeeper:

`spctl --master-disable`

- Add a rule to allow an application to run (labeling of rule is optional):

`spctl --add --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Turn on Gatekeeper:

`spctl --master-enable`

- List all rules on the system:

`spctl --list`
