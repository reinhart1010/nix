---
layout: page
title: linux/lsb_release (English)
description: "Provides certain LSB (Linux Standard Base) and distribution-specific information."
content_hash: aff3b95e1913f81dc165c9e4f1b50a836507fefb
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/lsb_release.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsb_release.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsb_release.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsb_release.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsb_release

Provides certain LSB (Linux Standard Base) and distribution-specific information.
More information: <https://manned.org/lsb_release>.

- Print all available information:

`lsb_release -a`

- Print a description (usually the full name) of the operating system:

`lsb_release -d`

- Print only the operating system name (ID), suppressing the field name:

`lsb_release -i -s`

- Print the release number and codename of the distribution, suppressing the field names:

`lsb_release -rcs`
