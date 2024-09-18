---
layout: page
title: linux/check-support-status (English)
description: "Identify installed Debian packages for which support has had to be limited or prematurely ended."
content_hash: d0e26220a3bae95b26e6c113cadaa8ecf675808c
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# check-support-status

Identify installed Debian packages for which support has had to be limited or prematurely ended.
More information: <https://manned.org/check-support-status>.

- Display packages whose support is limited, has already ended or will end earlier than the distribution's end of life:

`check-support-status`

- Display only packages whose support has ended:

`check-support-status --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ended</span>

- Skip printing a headline:

`check-support-status --no-heading`
