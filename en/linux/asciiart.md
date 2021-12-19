---
layout: page
title: linux/asciiart (English)
description: "Convert images to ASCII."
content_hash: 2ce935f2872dfc84d2f70e9cc4add88fedf02ee8
related_topics:
  - title: Deutsch version
    url: /de/linux/asciiart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/asciiart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/asciiart.html
    icon: bi bi-globe
---
# asciiart

Convert images to ASCII.
More information: <https://github.com/nodanaonlyzuul/asciiart>.

- Read an image from a file and print in ASCII:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Read an image from a URL and print in ASCII:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/image.jpg</span>

- Choose the output width (default is 100):

`asciiart --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Colorize the ASCII output:

`asciiart --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Choose the output format (default format is text):

`asciiart --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Invert the character map:

`asciiart --invert-chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>
