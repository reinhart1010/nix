---
layout: page
title: osx/xattr (English)
description: "Utility to work with extended filesystem attributes."
content_hash: b47b316ea74c27cceb636f5204d0544774fb3647
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/xattr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xattr

Utility to work with extended filesystem attributes.
More information: <https://ss64.com/osx/xattr.html>.

- List key:value extended attributes for a given file:

`xattr -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Write an attribute for a given file:

`xattr -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Delete an attribute from a given file:

`xattr -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.quarantine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Delete all extended attributes from a given file:

`xattr -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Recursively delete an attribute in a given directory:

`xattr -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>
