---
layout: page
title: common/scan-build (English)
description: "Command-line utility to run a static analyzer over a codebase as part of performing a regular build."
content_hash: 86487d78fa554d3434b76432571092c3a2962606
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# scan-build

Command-line utility to run a static analyzer over a codebase as part of performing a regular build.
More information: <https://clang-analyzer.llvm.org/scan-build.html>.

- Build and analyze the project in the current directory:

`scan-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Run a command and pass all subsequent options to it:

`scan-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Display help:

`scan-build`
