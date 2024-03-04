---
layout: page
title: common/pnpm-outdated (English)
description: "Check for outdated packages."
content_hash: f89c2647e7391095303cfb59992e04117b4ae9f5
last_modified_at: 2024-03-04
tldri18n_status: 2
---
# pnpm outdated

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
