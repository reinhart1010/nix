---
layout: page
title: common/disown (हिन्दी)
description: "उप-प्रक्रियाओं को उस शेल से परे रहने की अनुमति दें जिससे वे जुड़े हुए हैं।"
content_hash: 5e0188e7a72d4bae831aa32b453e239a8209757c
last_modified_at: 2024-10-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/disown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># disown

उप-प्रक्रियाओं को उस शेल से परे रहने की अनुमति दें जिससे वे जुड़े हुए हैं।
`jobs` कमांड भी देखें।
अधिक जानकारी: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>।

- वर्तमान कार्य को अस्वीकार करें:

`disown`

- किसी विशिष्ट कार्य को अस्वीकार करे:

`disown %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कार्य_की_संख्या</span>

- सभी कार्य को अस्वीकार करें:

`disown -a`

- कार्य को रखें (इसे अस्वीकार न करें), लेकिन इसे चिह्नित करें ताकि भविष्य में शेल निकास पर कोई SIGHUP प्राप्त न हो।:

`disown -h %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कार्य_की_संख्या</span>
