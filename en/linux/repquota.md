---
layout: page
title: linux/repquota (English)
description: "Display a summary of existing file quotas for a filesystem."
content_hash: 852bd4b7d17116c569acfcd291711dece6566b21
---
# repquota

Display a summary of existing file quotas for a filesystem.
More information: <https://manned.org/repquota>.

- Report stats for all quotas in use:

`sudo repquota -all`

- Report quota stats for all users, even those who aren't using any of their quota:

`sudo repquota -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem</span>

- Report on quotas for users only:

`repquota --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem</span>

- Report on quotas for groups only:

`sudo repquota --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem</span>

- Report on used quota and limits in a human-readable format:

`sudo repquota --human-readable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem</span>

- Report on all quotas for users and groups in a human-readable format:

`sudo repquota -augs`
