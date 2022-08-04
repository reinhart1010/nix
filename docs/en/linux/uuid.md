---
layout: page
title: linux/uuid (English)
description: "Generate and decode Universally Unique Identifiers (UUID)."
content_hash: 71115e3072e85c9907f3649e40d20083b325eab6
---
# uuid

Generate and decode Universally Unique Identifiers (UUID).
See also `uuidgen`.
More information: <https://manned.org/uuid>.

- Generate a UUIDv1 (based on time and system's hardware address, if present):

`uuid`

- Generate a UUIDv4 (based on random data):

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Generate multiple UUIDv4 identifiers at once:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_uuids</span>

- Generate a UUIDv4 and specify the output format:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BIN|STR|SIV</span>

- Generate a UUIDv4 and write the output to a file:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a UUIDv5 (based on the supplied object name) with a specified namespace prefix:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` ns:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DNS|URL|OID|X500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_name</span>

- Decode a given UUID:

`uuid -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>
