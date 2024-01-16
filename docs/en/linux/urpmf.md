---
layout: page
title: linux/urpmf (English)
description: "Find files in packages and query information about them in Mageia."
content_hash: 46427d2fc0cb567ffd2d04e4f46885065084bfa7
last_modified_at: 2024-01-16
tldri18n_status: 2
---
# urpmf

Find files in packages and query information about them in Mageia.
See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmi.update`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- Search for packages that contain a file:

`urpmf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Search for packages that contain both a keyword [a]nd another in their summaries:

`urpmf --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword2</span>

- Search for packages that contain a keyword [o]r another in their descriptions:

`urpmf --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword1</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword2</span>

- Search for packages that do not contain a keyword in their name ignoring case distinction using "|" as the [F]ield separator (":" by default):

`urpmf --description ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` -F'|'`
