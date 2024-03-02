---
layout: page
title: common/duf (English)
description: "Disk Usage/Free Utility."
content_hash: efde5e26ed54cc59180f846a5f707a009e38f635
last_modified_at: 2024-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/duf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duf

Disk Usage/Free Utility.
More information: <https://github.com/muesli/duf>.

- List accessible devices:

`duf`

- List everything (such as pseudo, duplicate or inaccessible file systems):

`duf --all`

- Only show specified devices or mount points:

`duf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Sort the output by a specified criteria:

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size|used|avail|usage</span>

- Show or hide specific filesystems:

`duf --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">only-fs|hide-fs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs|vfat|ext4|xfs</span>

- Sort the output by key:

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem</span>

- Change the theme (if `duf` fails to use the right theme):

`duf --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dark|light</span>
