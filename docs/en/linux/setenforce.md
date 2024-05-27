---
layout: page
title: linux/setenforce (English)
description: "Toggle SELinux between enforcing and permissive modes."
content_hash: 673e26b3d12bc52e81e47b9110e10ba23036552b
last_modified_at: 2024-05-27
tldri18n_status: 2
---
# setenforce

Toggle SELinux between enforcing and permissive modes.
To enable or disable SELinux, edit `/etc/selinux/config` instead.
See also: `getenforce`, `semanage-permissive`.
More information: <https://manned.org/man/setenforce>.

- Put SELinux in enforcing mode:

`setenforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|Enforcing</span>

- Put SELiunx in permissive mode:

`setenforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|Permissive</span>
