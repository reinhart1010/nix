---
layout: page
title: linux/aurvote (English)
description: "Vote for packages in the Arch User Repository."
content_hash: 3018c62c54109aa23b251e146d761632cf5f7ed9
last_modified_at: 2023-12-27
related_topics:
  - title: 中文 version
    url: /zh/linux/aurvote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aurvote

Vote for packages in the Arch User Repository.
To be able to vote, the file `~/.config/aurvote` must exist and contain your AUR credentials.
More information: <https://github.com/archlinuxfr/aurvote>.

- Interactively create the file `~/.config/aurvote` containing your AUR username and password:

`aurvote --configure`

- Vote for one or more AUR packages:

`aurvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Unvote one or more AUR packages:

`aurvote --unvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Check if one or more AUR packages have already been voted:

`aurvote --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Display help:

`aurvote --help`
