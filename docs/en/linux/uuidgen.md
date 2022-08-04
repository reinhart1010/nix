---
layout: page
title: linux/uuidgen (English)
description: "Generate unique identifiers (UUIDs)."
content_hash: 92fc000764437f40e62c4a8c3b3aaa175aa6909b
---
# uuidgen

Generate unique identifiers (UUIDs).
See also `uuid`.
More information: <https://manned.org/uuidgen>.

- Create a random UUIDv4:

`uuidgen --random`

- Create a UUIDv1 based on the current time:

`uuidgen --time`

- Create a UUIDv5 of the name with a specified namespace prefix:

`uuidgen --sha1 --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@dns|@url|@oid|@x500</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_name</span>
