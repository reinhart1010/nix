---
layout: page
title: linux/google-chrome (English)
description: "The web browser from Google."
content_hash: d2c52e1afae8cca054b484494d22622575adc1a7
related_topics:
  - title: Deutsch version
    url: /de/linux/google-chrome.html
    icon: bi bi-globe
---
# google-chrome

The web browser from Google.
More information: <https://chrome.google.com>.

- Run with a custom profile directory:

`google-chrome --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run without CORS validation, useful to test an API:

`google-chrome --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --disable-web-security`
