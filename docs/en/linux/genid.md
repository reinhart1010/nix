---
layout: page
title: linux/genid (English)
description: "Generate IDs, such as snowflakes, UUIDs, and a new GAID."
content_hash: f7e3824660a928bbd3d4b819d664d95f35e6b51e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# genid

Generate IDs, such as snowflakes, UUIDs, and a new GAID.
More information: <https://github.com/bleonard252/genid>.

- Generate a UUIDv4:

`genid uuid`

- Generate a UUIDv5 using a namespace UUID and a specific name:

`genid uuidv5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{ce598faa-8dd0-49ee-8525-9e24fff71dca}</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Generate a Discord Snowflake, without a trailing newline (useful in shell scripts):

`genid --script snowflake`

- Generate a Generic Anonymous ID with a specific "real ID":

`genid gaid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">real_id</span>

- Generate a Snowflake with the epoch set to a specific date:

`genid snowflake --epoch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unix_epoch_time</span>
