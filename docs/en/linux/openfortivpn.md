---
layout: page
title: linux/openfortivpn (English)
description: "A VPN client, for Fortinet's proprietary PPP+SSL VPN solution."
content_hash: 736201e91aad077a33e35042174046d3375fb15f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# openfortivpn

A VPN client, for Fortinet's proprietary PPP+SSL VPN solution.
More information: <https://github.com/adrienverge/openfortivpn>.

- Connect to a VPN with a username and password:

`openfortivpn --username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Connect to a VPN using a specific configuration file (defaults to `/etc/openfortivpn/config`):

`sudo openfortivpn --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>

- Connect to a VPN by specifying the host and port:

`openfortivpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Trust a given gateway by passing in its certificate's sha256 sum:

`openfortivpn --trusted-cert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256_sum</span>
