---
layout: page
title: linux/choom (English)
description: "Display and change the adjust out-of-memory killer score."
content_hash: 4b13261b86fcfd7b8fb4ce465b993f7395cd3c57
last_modified_at: 2024-03-16
tldri18n_status: 2
---
# choom

Display and change the adjust out-of-memory killer score.
More information: <https://manned.org/choom>.

- Display the OOM-killer score of the process with a specific ID:

`choom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Change the adjust OOM-killer score of a specific process:

`choom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1000..+1000</span>

- Run a command with a specific adjust OOM-killer score:

`choom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1000..+1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>
