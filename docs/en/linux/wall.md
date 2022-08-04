---
layout: page
title: linux/wall (English)
description: "Write a message on the terminals of users currently logged in."
content_hash: c5d32982676a390cad8893a935da72ba2a0de6c4
---
# wall

Write a message on the terminals of users currently logged in.
More information: <https://manned.org/wall>.

- Send a message:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" | wall`

- Send a message from a file:

`wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Send a message with timeout (default 300):

`wall -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
