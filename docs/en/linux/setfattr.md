---
layout: page
title: linux/setfattr (English)
description: "Set extended file attributes."
content_hash: 13d6d353ef22eeed23b8547aa3ac7e5f2774db18
last_modified_at: 2024-10-03
tldri18n_status: 2
---
# setfattr

Set extended file attributes.
More information: <https://manned.org/setfattr>.

- Set name of attribute for file:

`setfattr -n user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Set a user-defined value of an extended attribute on a file:

`setfattr -n user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_name</span>` -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove a specific attribute of a file:

`setfattr -x user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
