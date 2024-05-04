---
layout: page
title: common/pants (English)
description: "Fast, scalable, user-friendly, open-source build and developer workflow tool."
content_hash: 2b7c3efa7843e7ede7ad791108bc03d859d660b7
last_modified_at: 2024-05-04
tldri18n_status: 2
---
# pants

Fast, scalable, user-friendly, open-source build and developer workflow tool.
More information: <https://www.pantsbuild.org/2.20/docs/using-pants/command-line-help>.

- List all targets:

`pants list ::`

- Run all tests:

`pants test ::`

- Fix, format, and lint only uncommitted files:

`pants --changed-since=HEAD fix fmt lint`

- Typecheck only uncommitted files and their dependents:

`pants --changed-since=HEAD --changed-dependents=transitive check`

- Create a distributable package for the specified target:

`pants package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory:target-name</span>

- Auto-generate BUILD file targets for new source files:

`pants tailor ::`

- Display help:

`pants help`
