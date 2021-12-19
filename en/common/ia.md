---
layout: page
title: common/ia (English)
description: "Command-line tool to interact with `archive.org`."
content_hash: 0aa619691a1d7abeb9ed2a511cc2a2a5aaee8a3f
---
# ia

Command-line tool to interact with `archive.org`.
More information: <https://archive.org/services/docs/api/internetarchive/cli.html>.

- Configure `ia` with API keys (some functions won't work without this step):

`ia configure`

- Upload one or more items to `archive.org`:

`ia upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --metadata="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mediatype:data</span>`" --metadata="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title:example</span>`"`

- Download one or more items from `archive.org`:

`ia download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item</span>

- Delete one or more items from `archive.org`:

`ia delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Search on `archive.org`, returning results as JSON:

`ia search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject:"subject" collection:collection</span>`'`
