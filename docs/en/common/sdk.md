---
layout: page
title: common/sdk (English)
description: "Manage parallel versions of multiple Software Development Kits."
content_hash: f725d62ddca5fae0de7111d0dbc3d8d2af057cee
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# sdk

Manage parallel versions of multiple Software Development Kits.
Supports Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x and many others.
More information: <https://sdkman.io/usage>.

- Install an SDK version:

`sdk install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_version</span>

- Use a specific SDK version for the current terminal session:

`sdk use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_version</span>

- Show the stable version of any available SDK:

`sdk current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>

- Show the stable versions of all installed SDKs:

`sdk current`

- List all available SDKs:

`sdk list`

- List all versions of an SDK:

`sdk list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>

- Upgrade an SDK to the latest stable version:

`sdk upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>

- Uninstall a specific SDK version:

`sdk rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_version</span>
