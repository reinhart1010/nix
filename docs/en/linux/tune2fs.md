---
layout: page
title: linux/tune2fs (English)
description: "Adjust parameters of an ext2, ext3 or ext4 filesystem."
content_hash: f15fc196f599b4aeb8a67e162661165fa3f57e8b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tune2fs

Adjust parameters of an ext2, ext3 or ext4 filesystem.
May be used on mounted filesystems.
More information: <https://manned.org/tune2fs>.

- Set the max number of counts before a filesystem is checked to 2:

`tune2fs -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Set the filesystem label to MY_LABEL:

`tune2fs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'MY_LABEL'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Enable discard and user-specified extended attributes for a filesystem:

`tune2fs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">discard,user_xattr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Enable journaling for a filesystem:

`tune2fs -o^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nobarrier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
