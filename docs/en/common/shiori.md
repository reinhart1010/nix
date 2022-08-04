---
layout: page
title: common/shiori (English)
description: "Simple bookmark manager built with Go."
content_hash: 7100f5230b00365c97cbb96c8b81cc084e1caddc
---
# shiori

Simple bookmark manager built with Go.
More information: <https://github.com/go-shiori/shiori>.

- Import bookmarks from HTML Netscape bookmark format file:

`shiori import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bookmarks.html</span>

- Save the specified URL as bookmark:

`shiori add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- List the saved bookmarks:

`shiori print`

- Open the saved bookmark in a browser:

`shiori open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bookmark_id</span>

- Start the web interface for managing bookmarks at port 8181:

`shiori serve --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8181</span>
