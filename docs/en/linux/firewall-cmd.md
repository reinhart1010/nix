---
layout: page
title: linux/firewall-cmd (English)
description: "The firewalld command-line client."
content_hash: 1ca36885c93983331d6208adb4de601e1c8d5853
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# firewall-cmd

The firewalld command-line client.
More information: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- View the available firewall zones:

`firewall-cmd --get-active-zones`

- View the rules which are currently applied:

`firewall-cmd --list-all`

- Permanently move the interface into the block zone, effectively blocking all communication:

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">block</span>` --change-interface=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enp1s0</span>

- Permanently open the port for a service in the specified zone (like port 443 when in the `public` zone):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --add-service=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https</span>

- Permanently close the port for a service in the specified zone (like port 80 when in the `public` zone):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --remove-service=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http</span>

- Permanently open two arbitrary ports in the specified zone:

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --add-port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25565/tcp</span>` --add-port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">19132/udp</span>

- Reload firewalld to force rule changes to take effect:

`firewall-cmd --reload`
