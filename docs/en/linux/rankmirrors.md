---
layout: page
title: linux/rankmirrors (English)
description: "Rank a list of Pacman mirrors by connection and opening speed."
content_hash: 3dd63783ecfdca91f2b9e3ac5c9d3b4a8e5d824b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rankmirrors

Rank a list of Pacman mirrors by connection and opening speed.
Writes the new mirrorlist to `stdout`.
More information: <https://wiki.archlinux.org/index.php/mirrors>.

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
