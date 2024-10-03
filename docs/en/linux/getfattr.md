---
layout: page
title: linux/getfattr (English)
description: "Display file names and extended attributes."
content_hash: bf3ccf100a46230fad2f13fd45a72acf07d08b8f
last_modified_at: 2024-10-03
tldri18n_status: 2
---
# getfattr

Display file names and extended attributes.
More information: <https://manned.org/getfattr>.

- Retrieve all extended attributes of a file and display them in a detailed format:

`getfattr -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Get a specific attribute of a file:

`getfattr -n user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
