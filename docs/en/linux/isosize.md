---
layout: page
title: linux/isosize (English)
description: "Display the size of an ISO file."
content_hash: 2a1c32eb27af9d5c3ef339e8230f93297275582b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# isosize

Display the size of an ISO file.
More information: <https://manned.org/isosize>.

- Display the size of an ISO file:

`isosize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iso</span>

- Display the block count and block size of an ISO file:

`isosize --sectors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iso</span>

- Display the size of an ISO file divided by a given number (only usable when --sectors is not given):

`isosize --divisor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iso</span>
