---
layout: page
title: linux/inxi (English)
description: "Print a summary of system information and resources for debugging purposes."
content_hash: 28cf6238b9833549796c7081e2a12c734d07e2e3
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/inxi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# inxi

Print a summary of system information and resources for debugging purposes.
More information: <https://manned.org/inxi>.

- Print a summary of CPU, memory, hard drive and kernel information:

`inxi`

- Print a full description of CPU, memory, disk, network, and process information and filter sensitive information:

`inxi --expanded --filter`

- Print a summary of CPU information:

`inxi --cpu`

- Print a summary of graphics information:

`inxi --graphics`

- Print a summary of system RAM:

`inxi --memory`

- Print a summary of system audio:

`inxi --audio`

- Print available sensor data:

`inxi --sensors`

- Print information about the distribution's repositories:

`inxi --repos`
