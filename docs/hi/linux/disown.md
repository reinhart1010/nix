---
layout: page
title: linux/disown (हिन्दी)
description: "उप-प्रक्रियाओं को उस शेल से परे रहने की अनुमति दें जिससे वे जुड़े हुए हैं।"
content_hash: 5e0188e7a72d4bae831aa32b453e239a8209757c
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/linux/disown.html
    icon: bi bi-globe
---
# disown

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
