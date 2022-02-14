---
layout: page
title: osx/plutil (English)
description: "View, convert, validate, or edit property list (\"plist\") files."
content_hash: 0a4eec8792bf4fc038eae9e3e560f808c281a4e6
---
# plutil

View, convert, validate, or edit property list ("plist") files.
More information: <https://www.manpagez.com/man/1/plutil/>.

- Display the contents of one or more plist files in human-readable format:

`plutil -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.plist file2.plist ...</span>

- Convert one or more plist files to XML format, overwriting the original files in-place:

`plutil -convert xml1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.plist file2.plist ...</span>

- Convert one or more plist files to binary format, overwriting the original files in-place:

`plutil -convert binary1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.plist file2.plist ...</span>

- Convert a plist file to a different format, writing to a new file:

`plutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml1|binary1|json|swift|objc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.plist</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_file.plist</span>

- Convert a plist file to a different format, writing to stdout:

`plutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml1|binary1|json|swift|objc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.plist</span>` -o -`
