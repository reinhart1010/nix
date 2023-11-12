---
layout: page
title: linux/kwrite (English)
description: "Text editor of the KDE Desktop project."
content_hash: 80336201cf53978d86a5f608daddde574bf98ce4
last_modified_at: 2023-11-12
related_topics:
  - title: മലയാളം version
    url: /ml/linux/kwrite.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kwrite

Text editor of the KDE Desktop project.
See also `kate`.
More information: <https://apps.kde.org/kwrite/>.

- Open a text file:

`kwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open multiple text files:

`kwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Open a text file with a specific encoding:

`kwrite --encoding=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a text file and navigate to a specific line and column:

`kwrite --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
