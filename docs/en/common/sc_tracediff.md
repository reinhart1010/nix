---
layout: page
title: common/sc_tracediff (English)
description: "Display traceroute paths where the path has changed."
content_hash: fe47f46002030d3878d4e7b5efc16f542baf446b
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# sc_tracediff

Display traceroute paths where the path has changed.
More information: <https://www.caida.org/catalog/software/scamper/>.

- Show the difference between traceroutes in two `warts` files:

`sc_tracediff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.warts</span>

- Show the difference between the traceroutes in two `warts` files, including those that have not changed:

`sc_tracediff -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.warts</span>

- Show the difference between the traceroutes in two `warts` files and try to show DNS names and not IP addresses if possible:

`sc_tracediff -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.warts</span>
