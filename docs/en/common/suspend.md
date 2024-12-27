---
layout: page
title: common/suspend (English)
description: "Suspend the execution of the current shell."
content_hash: 84facb9c8bd8031f785f872d9696ad3dd2a25830
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# suspend

Suspend the execution of the current shell.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

- Suspend the current shell (useful for when you are in nested shells like `su`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>` <Enter> suspend`

- Run in a separate terminal to continue from suspension if `suspend` was used in a non-nested shell:

`pkill -CONT bash`

- Force suspension even if this would lock you out of the system:

`suspend -f`
