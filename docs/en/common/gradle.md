---
layout: page
title: common/gradle (English)
description: "An open source build automation system."
content_hash: 4ef432b029caf66afbd6794aef802409de3ac6b3
last_modified_at: 2023-11-15
related_topics:
  - title: español version
    url: /es/common/gradle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gradle

An open source build automation system.
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
