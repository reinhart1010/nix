---
layout: page
title: linux/expect (English)
description: "Script executor that interacts with other programs that require user input."
content_hash: 624db85727e18034fb030dc60872e872fc68ce49
---
# expect

Script executor that interacts with other programs that require user input.
More information: <https://manned.org/expect>.

- Execute an expect script from a file:

`expect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Execute a specified expect script:

`expect -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commands</span>`"`

- Enter an interactive REPL (use `exit` or Ctrl + D to exit):

`expect -i`
