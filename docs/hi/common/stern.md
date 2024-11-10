---
layout: page
title: common/stern (हिन्दी)
description: "Kubernetes से कई पॉड और कंटेनरों का टेल करें।"
content_hash: d2c362d8d7b8209c4592f6db32474d4c737223eb
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stern.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stern.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stern

Kubernetes से कई पॉड और कंटेनरों का टेल करें।
अधिक जानकारी: <https://github.com/stern/stern>।

- वर्तमान नामस्थान में सभी पॉड्स का टेल करें:

`stern .`

- एक विशिष्ट स्थिति वाले सभी पॉड्स का टेल करें:

`stern . --container-state `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">चल रहा है|इंतज़ार कर रहा है|समाप्त हुआ</span>

- एक दिए गए नियमित अभिव्यक्ति से मेल खाने वाले सभी पॉड्स का टेल करें:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पॉड_क्वेरी</span>

- सभी नामस्थान से मेल खाने वाले पॉड्स का टेल करें:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पॉड_क्वेरी</span>` --all-namespaces`

- 15 मिनट पहले के मेल खाने वाले पॉड्स का टेल करें:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पॉड_क्वेरी</span>` --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15m</span>

- एक विशिष्ट लेबल वाले मेल खाने वाले पॉड्स का टेल करें:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पॉड_क्वेरी</span>` --selector `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release=canary</span>
