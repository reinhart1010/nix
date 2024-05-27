---
layout: page
title: linux/urpmi.addmedia (English)
description: "Add media in Mageia."
content_hash: 1c2643310faa09ea041caafa95dfd37d6a2edac4
last_modified_at: 2024-05-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urpmi.addmedia.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urpmi.addmedia

Add media in Mageia.
Note: Mageia documentation uses medium and repository as synonymous.
See also: `urpmi`, `urpmi.update`, `urpme`, `urpmi.removemedia`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpme>.

- Add a medium:

`sudo urpmi.addmedia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">medium</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp://ftp.site.com/path/to/Mageia/RPMS</span>

- Add a medium from a hard drive (run `genhdlist2` in the directory first):

`sudo urpmi.addmedia --distrib HD file:/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/repo</span>

- Add important media from a chosen mirror:

`sudo urpmi.addmedia --distrib ftp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mirror_website}/mirror/mageia/distrib/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch</span>

- Automatically select mirrors from a mirror list:

`sudo urpmi.addmedia --distrib --mirrorlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mirrorlist</span>
