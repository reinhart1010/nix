---
layout: page
title: linux/sleep (English)
description: "Delay for a specified amount of time."
content_hash: ab6456b3cae6e8e997e7129f2e48c86a32b4bce9
last_modified_at: 2023-02-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sleep

Delay for a specified amount of time.
More information: <https://www.gnu.org/software/coreutils/sleep>.

- Delay in seconds:

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>

- Delay in [m]inutes. (Other units [d]ay, [h]our, [s]econd, [inf]inity can also be used):

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m`

- Delay for 1 [d]ay 3 [h]ours:

`sleep 1d 3h`

- Execute a specific command after 20 [m]inutes delay:

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
