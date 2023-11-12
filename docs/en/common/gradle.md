---
layout: page
title: common/gradle (English)
description: "Gradle is an open source build automation system."
content_hash: 3102adc84356d1bb31af5fa96b7f0a610d54fe7c
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/gradle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gradle

Gradle is an open source build automation system.
More information: <https://gradle.org>.

- Compile a package:

`gradle build`

- Exclude test task:

`gradle build -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test</span>

- Run in offline mode to prevent Gradle from accessing the network during builds:

`gradle build --offline`

- Clear the build directory:

`gradle clean`

- Build an Android Package (APK) in release mode:

`gradle assembleRelease`

- List the main tasks:

`gradle tasks`

- List all the tasks:

`gradle tasks --all`
