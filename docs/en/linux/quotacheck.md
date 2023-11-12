---
layout: page
title: linux/quotacheck (English)
description: "Scan a filesystem for disk usage; create, check and repair quota files."
content_hash: 2b10da442c1c07b16976965b451ab127489ec885
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# quotacheck

Scan a filesystem for disk usage; create, check and repair quota files.
It is best to run quota check with quotas turned off to prevent damage or loss to quota files.
More information: <https://manned.org/quotacheck>.

- Check quotas on all mounted non-NFS filesystems:

`sudo quotacheck --all`

- Force check even if quotas are enabled (this can cause damage or loss to quota files):

`sudo quotacheck --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Check quotas on a given filesystem in debug mode:

`sudo quotacheck --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Check quotas on a given filesystem, displaying the progress:

`sudo quotacheck --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Check user quotas:

`sudo quotacheck --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Check group quotas:

`sudo quotacheck --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>
