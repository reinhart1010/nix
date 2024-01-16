---
layout: page
title: linux/urpmi-removemedia (English)
description: "Remove media in Mageia."
content_hash: 483982ade14a6730f62d771023086196ddba7f7a
last_modified_at: 2024-01-16
tldri18n_status: 2
---
# urpmi.removemedia

Remove media in Mageia.
NOTE: Mageia documentation uses medium and repository as synonymous.
See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.update`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- Remove a medium:

`sudo urpmi.removemedia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">medium</span>

- Remove all media:

`sudo urpmi.removemedia -a`

- Remove media fuzz[y] matching on media names:

`sudo urpmi.removemedia -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>
