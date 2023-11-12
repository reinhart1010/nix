---
layout: page
title: common/security-checker (English)
description: "Check if a PHP application uses dependencies with known security vulnerabilities."
content_hash: ef33a45998a10bb04a4934ab403ed7988d1bbd56
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# security-checker

Check if a PHP application uses dependencies with known security vulnerabilities.
More information: <https://github.com/sensiolabs/security-checker>.

- Look for security issues in the project dependencies (based on the `composer.lock` file in the current directory):

`security-checker security:check`

- Use a specific `composer.lock` file:

`security-checker security:check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/composer.lock</span>

- Return results as a JSON object:

`security-checker security:check --format=json`
