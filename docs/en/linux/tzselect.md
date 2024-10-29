---
layout: page
title: linux/tzselect (English)
description: "Interactively select timezone."
content_hash: 472047d92607cd57e15f1641899f7f480f2e7b92
last_modified_at: 2024-10-29
tldri18n_status: 2
---
# tzselect

Interactively select timezone.
Note: this program doesn't actually set the timezone.
More information: <https://manned.org/tzselect>.

- Open the interactive menu for timezone selection and print the selected timezone to `stdout`:

`tzselect`

- Ask for nearest timezone to coordinates in ISO 6709 notation:

`tzselect -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">coordinates</span>
