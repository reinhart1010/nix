---
layout: page
title: common/surfraw (English)
description: "CLI to query a variety of web search engines."
content_hash: 6e22ebc08091e09f3d8510cea683fd6c4de6bfce
---
# surfraw

CLI to query a variety of web search engines.
Consists of a collection of elvi, each of which knows how to search a specific website.
More information: <http://surfraw.org>.

- Display the list of supported website search scripts (elvi):

`surfraw -elvi`

- Open the elvi's results page for a specific search in the browser:

`surfraw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elvi</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>`"`

- Display an elvi description and its specific options:

`surfraw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elvi</span>` -local-help`

- Search using an elvi with specific options and open the results page in the browser:

`surfraw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elvi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elvi_options</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>`"`

- Display the URL to the elvi's results page for a specific search:

`surfraw -print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elvi</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>`"`

- Search using the alias:

`sr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elvi</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>`"`
