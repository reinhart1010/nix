---
layout: page
title: linux/rankmirrors (English)
description: "Rank a list of Pacman mirrors by connection and opening speed."
content_hash: 67be4f1dd37a6aa010e2b960757e8f40b86c9e65
last_modified_at: 2024-09-25
tldri18n_status: 2
---
# rankmirrors

Rank a list of Pacman mirrors by connection and opening speed.
Writes the new mirrorlist to `stdout`.
More information: <https://manned.org/rankmirrors>.

- Rank a mirror list:

`rankmirrors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- Output only a given number of the top ranking servers:

`rankmirrors -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- Be verbose when generating the mirrorlist:

`rankmirrors -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- Test only a specific URL:

`rankmirrors --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Output only the response times instead of a full mirrorlist:

`rankmirrors --times `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>
