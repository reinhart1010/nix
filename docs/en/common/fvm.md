---
layout: page
title: common/fvm (English)
description: "Flutter version manager."
content_hash: 8aa4d6469771fcb8b63e462552e6e2c4375370eb
last_modified_at: 2024-02-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fvm

Flutter version manager.
More information: <https://fvm.app/documentation/guides/basic-commands>.

- Install a version of the Flutter SDK. Use without `version` for project settings:

`fvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Set a specific version of Flutter SDK in a project:

`fvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>

- Set a global version of the Flutter SDK:

`fvm global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Delete the FVM cache:

`fvm destroy`

- Remove a specific version of the Flutter SDK:

`fvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- List all installed versions of the Flutter SDK:

`fvm list`

- List all releases of the Flutter SDK:

`fvm releases`
