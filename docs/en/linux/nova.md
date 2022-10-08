---
layout: page
title: linux/nova (English)
description: "The OpenStack project that provides a way to provision compute instances."
content_hash: 31c72c7c9443d64fdc2ce73ce17bd34569fb7fbe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nova

The OpenStack project that provides a way to provision compute instances.
More information: <https://docs.openstack.org/nova/latest/>.

- List VMs on current tenant:

`nova list`

- List VMs of all tenants (admin user only):

`nova list --all-tenants`

- Boot a VM on a specific host:

`nova boot --nic net-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net_id</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_id</span>` --flavor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">flavor</span>` --availability-zone nova:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Start a server:

`nova start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Stop a server:

`nova stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Attach a network interface to a specific VM:

`nova interface-attach --net-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>
