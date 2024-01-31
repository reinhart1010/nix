---
layout: page
title: common/php (English)
description: "PHP command-line interface."
content_hash: 01070fedc3bd3596d31109d1bf1b6db921256020
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/common/php.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/php.html
    icon: bi bi-globe
tldri18n_status: 2
---
# php

PHP command-line interface.
More information: <https://php.net>.

- Parse and execute a PHP script:

`php `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check syntax on (i.e. lint) a PHP script:

`php -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run PHP interactively:

`php -a`

- Run PHP code (Notes: Don't use <? ?> tags; escape double quotes with backslash):

`php -r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Start a PHP built-in web server in the current directory:

`php -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host:port</span>

- List installed PHP extensions:

`php -m`

- Display information about the current PHP configuration:

`php -i`

- Display information about a specific function:

`php --rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function_name</span>
