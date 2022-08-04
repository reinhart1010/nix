---
layout: page
title: common/xidel (English)
description: "Download and extract data from HTML/XML pages as well as JSON APIs."
content_hash: 3e8b87b09ae192f46a0cfdc970e3c4c3a7c96459
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xidel

Download and extract data from HTML/XML pages as well as JSON APIs.
More information: <https://www.videlibri.de/xidel.html>.

- Print all URLs found by a Google search:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/search?q=test</span>` --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- Print the title of all pages found by a Google search and download them:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/search?q=test</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']</span>`" --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//title</span>` --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{$host}/'</span>

- Follow all links on a page and print the titles, with XPath:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//a</span>` --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//title</span>

- Follow all links on a page and print the titles, with CSS selectors:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">css('a')</span>`" --css `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>

- Follow all links on a page and print the titles, with pattern matching:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a>{.}</a>*</span>`" --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><title>{.}</title></span>`"`

- Read the pattern from example.xml (which will also check if the element containing "ood" is there, and fail otherwise):

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/example.xml</span>` --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><x><foo>ood</foo><bar>{.}</bar></x></span>`"`

- Print all newest Stack Overflow questions with title and URL using pattern matching on their RSS feed:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://stackoverflow.com/feeds</span>` --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+</span>`"`

- Check for unread Reddit mail, Webscraping, combining CSS, XPath, JSONiq, and automatically form evaluation:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://reddit.com</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})</span>`" --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">css('#mail')/@title</span>`"`
