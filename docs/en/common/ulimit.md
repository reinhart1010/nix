---
layout: page
title: common/ulimit (English)
description: "Get and set user limits."
content_hash: ce617ab09d2a15235d1f6e6441a34d7beb995c97
---
# ulimit

Get and set user limits.
More information: <https://manned.org/ulimit>.

- Get the properties of all the user limits:

`ulimit -a`

- Get hard limit for the number of simultaneously opened files:

`ulimit -H -n`

- Get soft limit for the number of simultaneously opened files:

`ulimit -S -n`

- Set max per-user process limit:

`ulimit -u 30`
