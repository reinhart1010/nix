---
layout: page
title: common/linode-cli-volumes (English)
description: "Manage Linode Volumes."
content_hash: d34399a0220aefdaa668c36e83b61949ef15df52
last_modified_at: 2023-09-17
---
# linode-cli volumes

Manage Linode Volumes.
See also: `linode-cli`.
More information: <https://www.linode.com/docs/products/tools/cli/guides/block-storage-volumes/>.

- List current Volumnes:

`linode-cli volumes list`

- Create a new Volume and attach it to a specific Linode:

`linode-cli volumes create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size_in_GB</span>` --linode-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Attach a Volume to a specific Linode:

`linode-cli volumes attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` --linode-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Detach a Volume from a Linode:

`linode-cli volumes detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>

- Resize a Volume (Note: size can only be increased):

`linode-cli volumes resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_size_in_GB</span>

- Delete a Volume:

`linode-cli volumes delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>
