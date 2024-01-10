---
layout: page
title: linux/libuser-lid (English)
description: "Display a user's groups or a group's users."
content_hash: 1b6b989ae174426bb36499535237806dba0f8964
last_modified_at: 2024-01-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/libuser-lid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libuser-lid

Display a user's groups or a group's users.
On Fedora and Arch Linux, this program is installed as `lid`.
More information: <https://manned.org/lid.8>.

- List primary and secondary groups of a specific user:

`sudo lid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List users of a specific group:

`sudo lid --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
