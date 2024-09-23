---
layout: page
title: linux/urpmi.addmedia (English)
description: "Add media in Mageia."
content_hash: b997d989cdea7fbda2cc558c19b07e213a3e6f0c
last_modified_at: 2024-09-23
tldri18n_status: 2
---
# urpmi.addmedia

Add media in Mageia.
Note: Mageia documentation uses medium and repository as synonymous.
See also: `urpmi`, `urpmi.update`, `urpme`, `urpmi.removemedia`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpme>.

- Add a medium:

`sudo urpmi.addmedia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">medium</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp://ftp.site.com/path/to/Mageia/RPMS</span>

- Add a medium from a hard drive (run `genhdlist2` in the directory first):

`sudo urpmi.addmedia --distrib HD file:/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/repo</span>

- Add important media from a chosen mirror:

`sudo urpmi.addmedia --distrib ftp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mirror_website</span>`/mirror/mageia/distrib/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch</span>

- Automatically select mirrors from a mirror list:

`sudo urpmi.addmedia --distrib --mirrorlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mirrorlist</span>
