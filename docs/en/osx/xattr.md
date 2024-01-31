---
layout: page
title: osx/xattr (English)
description: "Utility to work with extended filesystem attributes."
content_hash: 23faf17e9e6783f65f9904c77f50a1063ab01623
last_modified_at: 2024-01-31
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
More information: <https://keith.github.io/xcode-man-pages/xattr.1.html>.

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
