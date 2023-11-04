---
layout: page
title: linux/bluetoothctl (हिन्दी)
description: "ब्लूटूथ उपकरणों का प्रबंधन करें।"
content_hash: 0241ba5fcb6c2b87b2bf55310ebe7a47723defe3
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothctl.html
    icon: bi bi-globe
---
# bluetoothctl

ब्लूटूथ उपकरणों का प्रबंधन करें।
अधिक जानकारी: <https://bitbucket.org/serkanp/bluetoothctl>.

- `bluetoothctl` शैल में प्रवेश करें:

`bluetoothctl`

- सभी ज्ञात उपकरणों की सूची दिखाएं:

`bluetoothctl devices`

- ब्लूटूथ नियंत्रक को चालने या बंद करें:

`bluetoothctl power `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- किसी उपकरण के साथ जोड़ें:

`bluetoothctl pair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- किसी उपकरण को हटाएं:

`bluetoothctl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- एक जुड़े हुए उपकरण से कनेक्ट करें:

`bluetoothctl connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- एक जुड़े हुए उपकरण से डिसकनेक्ट करें:

`bluetoothctl disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- मदद दिखाएं:

`bluetoothctl help`
