---
layout: page
title: common/hostess (English)
description: "An idempotent command-line utility for managing the `/etc/hosts` file."
content_hash: 04892c3067848403bf54938ba946bc7e69f34a93
---
# hostess

An idempotent command-line utility for managing the `/etc/hosts` file.
More information: <https://github.com/cbednarski/hostess>.

- List domains, target IP addresses and on/off status:

`hostess list`

- Add a domain pointing to your machine to your hosts file:

`hostess add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local.example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>

- Remove a domain from your hosts file:

`hostess del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local.example.com</span>

- Disable a domain (but don't remove it):

`hostess off `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local.example.com</span>
