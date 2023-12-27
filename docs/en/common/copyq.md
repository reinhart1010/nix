---
layout: page
title: common/copyq (English)
description: "Clipboard manager with advanced features."
content_hash: 6762818a35c236ebea481ef25a123ac5e653c099
last_modified_at: 2023-12-27
related_topics:
  - title: 한국어 version
    url: /ko/common/copyq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# copyq

Clipboard manager with advanced features.
More information: <https://copyq.readthedocs.io/en/latest/command-line.html>.

- Launch CopyQ to store clipboard history:

`copyq`

- Show current clipboard content:

`copyq clipboard`

- Insert raw text into the clipboard history:

`copyq add -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text3</span>

- Insert text containing escape sequences ('\n', '\t') into the clipboard history:

`copyq add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firstline\nsecondline</span>

- Print the content of the first 3 items in the clipboard history:

`copyq read 0 1 2`

- Copy a file's contents into the clipboard:

`copyq copy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Copy a JPEG image into the clipboard:

`copyq copy image/jpeg < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>
