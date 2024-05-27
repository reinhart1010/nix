---
layout: page
title: linux/urpmi.removemedia (English)
description: "Remove media in Mageia."
content_hash: 05d14d0749266dd170affe03fabec34f6678759b
last_modified_at: 2024-05-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urpmi.removemedia.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urpmi.removemedia

Remove media in Mageia.
Note: Mageia documentation uses medium and repository as synonymous.
See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.update`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- Remove a medium:

`sudo urpmi.removemedia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">medium</span>

- Remove all media:

`sudo urpmi.removemedia -a`

- Remove media fuzz[y] matching on media names:

`sudo urpmi.removemedia -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>
