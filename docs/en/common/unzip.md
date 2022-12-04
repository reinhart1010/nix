---
layout: page
title: common/unzip (English)
description: "Extract compressed files in a ZIP archive."
content_hash: 0a29feb450878f5aebc448e2c57e1b2a4abbe9d3
last_modified_at: 2022-12-04
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/unzip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
---
# unzip

Extract compressed files in a ZIP archive.
More information: <https://manned.org/unzip>.

- Extract zip file(s) (for multiple files, separate file paths by spaces):

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file(s)</span>

- Extract zip files(s) to given path:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed_file(s)</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/put/extracted_file(s)</span>

- List the contents of a zip file without extracting:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.zip</span>

- Extract the contents of the file(s) to `stdout` alongside the extracted file names:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.zip</span>

- Extract a zip file created on Windows, containing files with non-ASCII (e.g. Chinese or Japanese characters) filenames:

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.zip</span>
