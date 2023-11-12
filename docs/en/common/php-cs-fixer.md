---
layout: page
title: common/php-cs-fixer (English)
description: "Automatic coding style fixer for PHP."
content_hash: 0d66cf5ba171b669cac46b94eb223cc849a8a854
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# PHP-CS-Fixer

Automatic coding style fixer for PHP.
More information: <https://github.com/FriendsOfPHP/PHP-CS-Fixer>.

- Execute code style fixing in the current directory:

`php-cs-fixer fix`

- Execute code style fixing for a specific directory:

`php-cs-fixer fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Execute code style linting without applying changes:

`php-cs-fixer fix --dry-run`

- Execute code style fixes using specific rules:

`php-cs-fixer fix --rules=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rules</span>

- Display the rules that have been applied:

`php-cs-fixer fix --verbose`

- Output the results in a different format:

`php-cs-fixer fix --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt|json|xml|checkstyle|junit|gitlab</span>

- Display files that require fixing:

`php-cs-fixer list-files`

- Describe a rule or ruleset:

`php-cs-fixer describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule</span>
