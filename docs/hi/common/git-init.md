---
layout: page
title: common/git-init (हिन्दी)
description: "एक नया स्थानीय गिट रिपॉजिटरी शुरू करता है।"
content_hash: 958f484547f0e44b1658b3ee93c13231ff0c2c20
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-init.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-init.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-init.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-init.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-init.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-init.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git init

एक नया स्थानीय गिट रिपॉजिटरी शुरू करता है।
अधिक जानकारी: <https://git-scm.com/docs/git-init>।

- एक नया स्थानीय भंडार शुरू करें:

`git init`

- प्रारंभिक शाखा के लिए निर्दिष्ट नाम के साथ एक भंडार शुरू करें:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">शाखा_का_नाम</span>

- ऑब्जेक्ट हैश के लिए SHA256 का उपयोग करके भंडार शुरू करें (गिट संस्करण २.२९+ की आवश्यकता है):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- एक अपूरित भंडार को शुरू करें, जो ssh के रिमोट के रूप में उपयोग के लिए उपयुक्त है:

`git init --bare`
