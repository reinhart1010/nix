---
layout: page
title: linux/firewall-cmd (English)
description: "The firewalld command-line client."
content_hash: fc57badf5240e4b4bd0e94f34ac8d93a222d93c1
last_modified_at: 2024-09-21
tldri18n_status: 2
---
# firewall-cmd

The firewalld command-line client.
View and adapt the runtime or permanent firewall configuration state.
More information: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- View all available firewall zones and rules in their runtime configuration state:

`firewall-cmd --list-all-zones`

- Permanently move the interface into the block zone, effectively blocking all communication:

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">block</span>` --change-interface=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enp1s0</span>

- Permanently open the port for a service in the specified zone (like port 443 when in the `public` zone):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --add-service=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https</span>

- Permanently close the port for a service in the specified zone (like port 80 when in the `public` zone):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --remove-service=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http</span>

- Permanently forward a port for incoming packets in the specified zone (like port 443 to 8443 when entering the `public` zone):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --add-rich-rule='rule family="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipv4|ipv6</span>`" forward-port port="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>`" protocol="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp|tcp</span>`" to-port="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8443</span>`"'`

- Reload firewalld to lose any runtime changes and force the permanent configuration to take effect immediately:

`firewall-cmd --reload`

- Save the runtime configuration state to the permanent configuration:

`firewall-cmd --runtime-to-permanent`

- Enable panic mode in case of Emergency. All traffic is dropped, any active connection will be terminated:

`firewall-cmd --panic-on`
