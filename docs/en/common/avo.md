---
layout: page
title: common/avo (English)
description: "The official command-line interface for Avo."
content_hash: 493e10029b9f500cbb3aad771d933c654ad2fcd4
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/avo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/avo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avo

The official command-line interface for Avo.
More information: <https://www.avo.app/docs/implementation/cli>.

- Initialize a workspace in the current directory:

`avo init`

- Log into the Avo platform:

`avo login`

- Switch to an existing Avo branch:

`avo checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Pull analytics wrappers for the current path:

`avo pull`

- Display the status of the Avo implementation:

`avo status`

- Resolve Git conflicts in Avo files:

`avo conflict`

- Open the current Avo workspace in the default web browser:

`avo edit`

- Display help for a subcommand:

`avo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
