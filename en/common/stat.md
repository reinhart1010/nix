---
layout: page
title: common/stat (English)
description: "Display file and filesystem information."
content_hash: 13ca6288688281bedf686ec1934fcbebab463745
---
# stat

Display file and filesystem information.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Show file properties such as size, permissions, creation and access dates among others:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Same as above but in a more concise way:

`stat -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show filesystem information:

`stat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show only octal file permissions:

`stat -c "%a %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show owner and group of the file:

`stat -c "%U %G" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show the size of the file in bytes:

`stat -c "%s %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
