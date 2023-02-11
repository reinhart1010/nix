---
layout: page
title: linux/wall (English)
description: "Write a message on the terminals of users currently logged in."
content_hash: 77e207d24b787f3c4afcc988d89b108828e8b946
last_modified_at: 2023-02-11
related_topics:
  - title: polski version
    url: /pl/linux/wall.html
    icon: bi bi-globe
---
# wall

Write a message on the terminals of users currently logged in.
More information: <https://manned.org/wall>.

- Send a message:

`wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Send a message to users that belong to a specific group:

`wall --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Send a message from a file:

`wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Send a message with timeout (default 300):

`wall --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
