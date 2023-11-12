---
layout: page
title: linux/wajig (English)
description: "Simplified all-in-one-place system support tool for Debian-based systems."
content_hash: 5bcf9d12d168506739fb7bb483e11ea897204e39
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/wajig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wajig

Simplified all-in-one-place system support tool for Debian-based systems.
More information: <https://wajig.togaware.com>.

- Update the list of available packages and versions:

`wajig update`

- Install a package, or update it to the latest available version:

`wajig install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its configuration files:

`wajig purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Perform an update and then a dist-upgrade:

`wajig daily-upgrade`

- Display the sizes of installed packages:

`wajig sizes`

- List the version and distribution for all installed packages:

`wajig versions`

- List versions of upgradable packages:

`wajig toupgrade`

- Display packages which have some form of dependency on the given package:

`wajig dependents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
