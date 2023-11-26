---
layout: page
title: linux/systemd-id128 (English)
description: "Generate and print sd-128 identifiers."
content_hash: 0984f1fcf6ac9cadfa5b121ccd0def04be37997e
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# systemd-id128

Generate and print sd-128 identifiers.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-id128.html>.

- Generate a new random identifier:

`systemd-id128 new`

- Print the identifier of the current machine:

`systemd-id128 machine-id`

- Print the identifier of the current boot:

`systemd-id128 boot-id`

- Print the identifier of the current service invocation (this is available in systemd services):

`systemd-id128 invocation-id`

- Generate a new random identifier and print it as a UUID (five groups of digits separated by hyphens):

`systemd-id128 new --uuid`
