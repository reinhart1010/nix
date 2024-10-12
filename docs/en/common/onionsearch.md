---
layout: page
title: common/onionsearch (English)
description: "Scrape URLs on different `.onion` search engines."
content_hash: cbc1630821627e2d59b4855098ce8fd602ebbc70
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# onionsearch

Scrape URLs on different `.onion` search engines.
Note: `onionsearch` requires a Tor proxy running on `localhost:9050`; a Tor enabled browser is needed to visit the `.onion` websites.
More information: <https://github.com/megadose/OnionSearch>.

- Request results from all the search engines:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`"`

- Request search results from specific search engines:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" --engines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tor66 deeplink phobos ...</span>

- Exclude certain search engines when searching:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">candle ahmia ...</span>

- Limit the number of pages to load per engine:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stuxnet</span>`" --engines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tor66 deeplink phobos ...</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- List all supported search engines:

`onionsearch --help | grep -A1 -i "supported engines"`
