---
layout: page
title: common/todo (தமிழ்)
description: "ஒரு எளிய, தரநிலை அடிப்படையிலான, cli todo மேலாளர்."
content_hash: 1e69d64ca7334e6055b8f64b68e853b1e95a0d0c
related_topics:
  - title: English version
    url: /en/common/todo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/todo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># todo

ஒரு எளிய, தரநிலை அடிப்படையிலான, cli todo மேலாளர்.
மேலும் விவரத்திற்கு: <https://todoman.readthedocs.io>.

- தொடங்கக்கூடிய பணிகளை பட்டியலிடுங்கள்:

`todo list --startable`

- பணி பட்டியலில் புதிய பணியைச் சேர்க்கவும்:

`todo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்ய_வேண்டியவை</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வேலை</span>

- கொடுக்கப்பட்ட ஐடியுடன் பணிக்கு இருப்பிடத்தைச் சேர்க்கவும்:

`todo edit --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இருப்பிட_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பணி_ஐடி</span>

- ஒரு பணியைப் பற்றிய விவரங்களைக் காட்டு:

`todo show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பணி_ஐடி</span>

- குறிப்பிட்ட ஐடிகளுடன் பணிகளை முடித்ததாகக் குறிக்கவும்:

`todo done `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பணி_ஐடி1 பணி_ஐடி2 ...</span>

- ஒரு பணியை நீக்கு:

`todo delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பணி_ஐடி</span>

- செய்த பணிகளை நீக்கி, மீதமுள்ள பணிகளின் ஐடிகளை மீட்டமைக்கவும்:

`todo flush`
