---
layout: page
title: common/copyq (English)
description: "Clipboard manager with advanced features."
content_hash: 1f4a0174e0fba5ba8ba9f597002684961c6c26ab
related_topics:
  - title: 한국어 version
    url: /ko/common/copyq.html
    icon: bi bi-globe
---
# copyq

Clipboard manager with advanced features.
More information: <https://hluk.github.io/CopyQ/>.

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

`copyq copy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>

- Copy a JPEG image into the clipboard:

`copyq copy image/jpeg < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.jpg</span>
