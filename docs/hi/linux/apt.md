---
layout: page
title: linux/apt (हिन्दी)
description: "डेबियन आधारित वितरणों के लिए पैकेज प्रबंधन उपयोगिता।"
content_hash: 249fa2e23fdc2ada9013491f9dd7150e56578971
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

डेबियन आधारित वितरणों के लिए पैकेज प्रबंधन उपयोगिता।
उबंटू संस्करण १६.०४ और बाद में इंटरैक्टिव रूप से उपयोग किए जाने पर `apt-get` के लिए अनुशंसित प्रतिस्थापन।
अन्य पैकेज प्रबंधकों में समतुल्य कमांड के लिए, देखें <https://wiki.archlinux.org/title/Pacman/Rosetta>।
अधिक जानकारी: <https://manned.org/apt.8>।

- उपलब्ध पैकेजों और संस्करणों की सूची को अपडेट करें (इसे अन्य `apt` कमांड से पहले चलाने की अनुशंसा की जाती है):

`sudo apt update`

- दिए गए पैकेज की खोज करें:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- दिए गए पैकेज के लिए जानकारी दिखाएं:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज इनस्टॉल करें, या इसे नवीनतम उपलब्ध संस्करण में अपडेट करें:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज निकालें (`remove` के बजाय `purge` का उपयोग करने से इसकी कॉन्फ़िगरेशन फ़ाइलें भी हट जाती हैं):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- सभी इनस्टॉल पैकेजों को उनके नवीनतम उपलब्ध संस्करणों में अपग्रेड करें:

`sudo apt upgrade`

- उपलब्ध, इन्सटाल्ड और अपग्रेड करने योग्य पैकेजों की सूची बनाएं:

`apt list`

- इन्सटाल्ड पैकेजों की सूची बनाएं:

`apt list --installed`
