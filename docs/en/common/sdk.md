---
layout: page
title: common/sdk (English)
description: "Tool for managing parallel versions of multiple Software Development Kits."
content_hash: 983d1dfe0317284e0619f8655b6f533815174ae2
---
# sdk

Tool for managing parallel versions of multiple Software Development Kits.
Supports Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x and many others.
More information: <https://sdkman.io/usage>.

- Install a specific version of Gradle:

`sdk install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle_version</span>

- Switch to a specific version of Gradle:

`sdk use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle_version</span>

- Check current Gradle version:

`sdk current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle</span>

- List all Software Development Kits available to install:

`sdk list`

- List all available versions for a specific Software Development Kit:

`sdk list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>

- List all installed Software Development Kits:

`sdk current`

- Update Gradle to the latest version:

`sdk upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle</span>

- Uninstall a particular version of Gradle:

`sdk rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gradle_version</span>
