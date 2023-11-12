---
layout: page
title: common/progress (English)
description: "Display/Monitor the progress of running coreutils."
content_hash: 5c700c5dc43910d5aeafbd07029da9c4f92bc946
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# progress

Display/Monitor the progress of running coreutils.
More information: <https://github.com/Xfennec/progress>.

- Show the progress of running coreutils:

`progress`

- Show the progress of running coreutils in quiet mode:

`progress -q`

- Launch and monitor a single long-running command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` & progress --monitor --pid $!`

- Include an estimate of time remaining for completion:

`progress --wait --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>
