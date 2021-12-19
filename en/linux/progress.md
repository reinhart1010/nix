---
layout: page
title: linux/progress (English)
description: "Display/Monitor the progress of running coreutils."
content_hash: 4954544aeaf2db10a85348718094e656cbe15ba2
---
# progress

Display/Monitor the progress of running coreutils.
More information: <https://github.com/Xfennec/progress>.

- Show the progress of running coreutils:

`progress`

- Show the progress of running coreutils in quiet mode:

`progress -q`

- Launch and monitor a single long-running command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` & progress -mp $!`
