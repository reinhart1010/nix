---
layout: page
title: common/amass-track (English)
description: "Track differences between enumerations of the same domain."
content_hash: e676953201df36559a903801ac553c90b5f8c146
---
# amass track

Track differences between enumerations of the same domain.
More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- Show the difference between the last two enumerations of the specified domain:

`amass track -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -last 2`

- Show the difference between a certain point in time and the last enumeration:

`amass track -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01/02 15:04:05 2006 MST</span>
