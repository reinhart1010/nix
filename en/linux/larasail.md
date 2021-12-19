---
layout: page
title: linux/larasail (English)
description: "A CLI tool for managing Laravel on Digital Ocean servers."
content_hash: 7ea9c7aed19f9d8e133673be4ea300246faaeeb8
---
# larasail

A CLI tool for managing Laravel on Digital Ocean servers.
More information: <https://github.com/thedevdojo/larasail>.

- Set up the server with Laravel dependencies using the default PHP version:

`larasail setup`

- Set up the server with Laravel dependencies using a specific PHP version:

`larasail setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php71</span>

- Add a new Laravel site:

`larasail host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/site_directory</span>

- Retrieve the Larasail user password:

`larasail pass`

- Retrieve the Larasail MySQL password:

`larasail mysqlpass`
