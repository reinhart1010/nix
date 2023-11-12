---
layout: page
title: common/phpenv (English)
description: "A PHP version manager for development purposes."
content_hash: d87fe0ef7753630027a3ccdda6d7913dbf627e4a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# phpenv

A PHP version manager for development purposes.
More information: <https://github.com/phpenv/phpenv>.

- Install a PHP version globally:

`phpenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Refresh shim files for all PHP binaries known to `phpenv`:

`phpenv rehash`

- List all installed PHP versions:

`phpenv versions`

- Display the currently active PHP version:

`phpenv version`

- Set the global PHP version:

`phpenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Set the local PHP version, which overrides the global version:

`phpenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Unset the local PHP version:

`phpenv local --unset`
