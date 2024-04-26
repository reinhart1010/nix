---
layout: page
title: linux/lsb_release (English)
description: "Get LSB (Linux Standard Base) and distribution-specific information."
content_hash: b7a67fe36a0d05b7a27414de87464b22e851fcca
last_modified_at: 2024-04-26
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

Get LSB (Linux Standard Base) and distribution-specific information.
More information: <https://manned.org/lsb_release>.

- Print all available information:

`lsb_release -a`

- Print a description (usually the full name) of the operating system:

`lsb_release -d`

- Print only the operating system name (ID), suppressing the field name:

`lsb_release -i -s`

- Print the release number and codename of the distribution, suppressing the field names:

`lsb_release -rcs`
