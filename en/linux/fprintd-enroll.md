---
layout: page
title: linux/fprintd-enroll (English)
description: "Enroll fingerprints into the database."
content_hash: 056a01824b14eec9d2e15b015d0a36f9281dcf0d
---
# fprintd-enroll

Enroll fingerprints into the database.
More information: <https://manned.org/fprintd-enroll>.

- Enroll the right index finger for the current user:

`fprintd-enroll`

- Enroll a specific finger for the current user:

`fprintd-enroll --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger</span>

- Enroll the right index finger for a specific user:

`fprintd-enroll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Enroll a specific finger for a specific user:

`fprintd-enroll --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">finger_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display help:

`fprintd-enroll --help`
