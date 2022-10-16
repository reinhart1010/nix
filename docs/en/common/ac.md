---
layout: page
title: common/ac (English)
description: "Print statistics on how long users have been connected."
content_hash: 660aa284f96ca8b33268d31efc9b7995d7bec29d
---
# ac

Print statistics on how long users have been connected.
More information: <https://man.openbsd.org/ac>.

- Print how long the current user has been connected in hours:

`ac`

- Print how long users have been connected in hours:

`ac -p`

- Print how long a particular user has been connected in hours:

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Print how long a particular user has been connected in hours per day (with total):

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
