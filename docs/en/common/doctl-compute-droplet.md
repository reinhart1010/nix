---
layout: page
title: common/doctl-compute-droplet (English)
description: "List, create, and delete virtual machines which are called droplets."
content_hash: 6dba8cc92470aac56dcde63b95e2e13d30056e78
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# doctl compute droplet

List, create, and delete virtual machines which are called droplets.
More information: <https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/>.

- Create a droplet:

`doctl compute droplet create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os_image</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vps_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">droplet_name</span>

- Delete a droplet:

`doctl compute droplet delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">droplet_id|droplet_name</span>

- List droplets:

`doctl compute droplet list`
