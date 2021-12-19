---
layout: page
title: linux/quotacheck (English)
description: "Scan a filesystem for disk usage; create, check and repair quota files."
content_hash: 58afc1021f04c5ac08e876ba6797a1fe7ce6deb8
---
# quotacheck

Scan a filesystem for disk usage; create, check and repair quota files.
It is best to run quota check with quotas turned off to prevent damage or loss to quota files.

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
