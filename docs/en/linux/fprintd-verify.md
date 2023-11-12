---
layout: page
title: linux/fprintd-verify (English)
description: "Verify fingerprints against the database."
content_hash: 10c38cf043cfeae053cf1f27debf2617382dc8c5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fprintd-verify

Verify fingerprints against the database.
More information: <https://manned.org/fprintd-verify>.

- Verify all stored fingerprints for the current user:

`fprintd-verify`

- Verify a specific fingerprint for the current user:

`fprintd-verify --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger</span>

- Verify fingerprints for a specific user:

`fprint-verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Verify a specific fingerprint for a specific user:

`fprintd-verify --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">finger_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Fail the process if a fingerprint doesn't match with ones stored in the database for the current user:

`fprint-verify --g-fatal-warnings`

- Display help:

`fprintd-verify --help`
