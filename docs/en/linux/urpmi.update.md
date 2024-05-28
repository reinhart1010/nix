---
layout: page
title: linux/urpmi.update (English)
description: "Update the list of packages from a package repository in Mageia."
content_hash: f11c954eb32c5068eb26cd607b3f39c3e3ceb5f6
last_modified_at: 2024-05-28
tldri18n_status: 2
---
# urpmi.update

Update the list of packages from a package repository in Mageia.
Note: Mageia documentation uses medium and repository as synonymous.
See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpmi.update>.

- Update all enabled media:

`urpmi.update -a`

- Update specific media (including disabled media):

`urpmi.update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">medium1 medium2 ...</span>

- Update all media that contain a specific keyword:

`urpmi.update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Update all configured media:

`urpmi.update e`
