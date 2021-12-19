---
layout: page
title: linux/check-support-status (English)
description: "Identify installed Debian packages for which support has had to be limited or prematurely ended."
content_hash: 600b6f967c9195ddc80460a452e21e36e9865dde
---
# check-support-status

Identify installed Debian packages for which support has had to be limited or prematurely ended.
More information: <https://manpages.debian.org/buster/debian-security-support/check-support-status.1.en.html>.

- Display packages whose support is limited, has already ended or will end earlier than the distribution's end of life:

`check-support-status`

- Display only packages whose support has ended:

`check-support-status --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ended</span>

- Skip printing a headline:

`check-support-status --no-heading`
