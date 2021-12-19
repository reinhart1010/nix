---
layout: page
title: linux/ncat (English)
description: "Use the normal `cat` functionality over networks."
content_hash: 962bebbb5605890349c5fd2996b0eda99a23f7d2
---
# ncat

Use the normal `cat` functionality over networks.

- Listen for input on the specified port and write it to the specified file:

`ncat -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Accept multiple connections and keep ncat open after they have been closed:

`ncat -lk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Write output of specified file to the specified host on the specified port:

`ncat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
