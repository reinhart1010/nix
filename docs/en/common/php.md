---
layout: page
title: common/php (English)
description: "PHP command-line interface."
content_hash: 0998ce23bab52d9a09e9c17c0931f2fe743a5cde
related_topics:
  - title: polski version
    url: /pl/common/php.html
    icon: bi bi-globe
---
# php

PHP command-line interface.
More information: <https://php.net>.

- Parse and execute a PHP script:

`php `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Check syntax on (i.e. lint) a PHP script:

`php -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Run PHP interactively:

`php -a`

- Run PHP code (Notes: Don't use <? ?> tags; escape double quotes with backslash):

`php -r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Start a PHP built-in web server in the current directory:

`php -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host:port</span>

- Get a list of installed PHP extensions:

`php -m`

- Display information about the current PHP configuration:

`php -i`

- Display information about a specific function:

`php --rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function_name</span>
