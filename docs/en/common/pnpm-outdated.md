---
layout: page
title: common/pnpm-outdated (English)
description: "Check for outdated packages."
content_hash: f89c2647e7391095303cfb59992e04117b4ae9f5
last_modified_at: 2024-03-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnpm-outdated.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnpm outdated

Check for outdated packages.
The check can be limited to a subset of the installed packages by providing arguments (patterns are supported).
More information: <https://pnpm.io/cli/outdated>.

- Check for outdated packages:

`pnpm outdated`

- Check for outdated dependencies found in every workspace package:

`pnpm outdated -r`

- Filter outdated packages using a package selector:

`pnpm outdated --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_selector</span>

- List outdated packages [g]lobally:

`pnpm outdated --global`

- Print details of outdated packages:

`pnpm outdated --long`

- Print outdated dependencies in a specific format:

`pnpm outdated --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>

- Print only versions that satisfy specifications in `package.json`:

`pnpm outdated --compatible`

- Check only outdated [D]ev dependencies:

`pnpm outdated --dev`
