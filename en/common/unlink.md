---
layout: page
title: common/unlink (English)
description: "Remove a link to a file from the filesystem."
content_hash: fbfca5668ba0729bf300d0dffef04fbae789944a
---
# unlink

Remove a link to a file from the filesystem.
The file contents is lost if the link is the last one to the file.
More information: <https://www.gnu.org/software/coreutils/unlink>.

- Remove the specified file if it is the last link:

`unlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
