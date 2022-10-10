---
layout: page
title: common/bazel (English)
description: "Open-source build and test tool similar to Make, Maven, and Gradle."
content_hash: 31f60002f26cb9c85b1053c6879b97208028eba5
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bazel

Open-source build and test tool similar to Make, Maven, and Gradle.
More information: <https://bazel.build/reference/command-line-reference>.

- Build the specified target in the workspace:

`bazel build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Remove output files and stop the server if running:

`bazel clean`

- Stop the bazel server:

`bazel shutdown`

- Display runtime info about the bazel server:

`bazel info`

- Display help:

`bazel help`

- Display version:

`bazel version`
