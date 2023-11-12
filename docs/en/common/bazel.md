---
layout: page
title: common/bazel (English)
description: "Open-source build and test tool similar to Make, Maven, and Gradle."
content_hash: 31f60002f26cb9c85b1053c6879b97208028eba5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# bazel

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
