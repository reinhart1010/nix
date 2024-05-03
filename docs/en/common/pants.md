---
layout: page
title: common/pants (English)
description: "Fast, scalable, user-friendly, open-source build and developer workflow tool."
content_hash: 2b7c3efa7843e7ede7ad791108bc03d859d660b7
last_modified_at: 2024-05-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pants.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pants

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
