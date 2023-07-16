---
layout: page
title: linux/larasail (English)
description: "Manage Laravel on Digital Ocean servers."
content_hash: b16ece02c7587b5dbc7170b4bcd9ff87974f2b04
last_modified_at: 2023-07-16
---
# larasail

Manage Laravel on Digital Ocean servers.
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
