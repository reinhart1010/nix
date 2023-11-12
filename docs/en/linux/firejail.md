---
layout: page
title: linux/firejail (English)
description: "Securely sandboxes processes to containers using built-in Linux capabilities."
content_hash: fa0ec865de0d5ae7bbf80ccbc7e2885edd0d0618
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# firejail

Securely sandboxes processes to containers using built-in Linux capabilities.
More information: <https://manned.org/firejail>.

- Integrate firejail with your desktop environment:

`sudo firecfg`

- Open a restricted Mozilla Firefox:

`firejail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Start a restricted Apache server on a known interface and address:

`firejail --net=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` --ip=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.244</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/init.d/apache2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start</span>

- List running sandboxes:

`firejail --list`

- List network activity from running sandboxes:

`firejail --netstats`

- Shutdown a running sandbox:

`firejail --shutdown=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7777</span>
