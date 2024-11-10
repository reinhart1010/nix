---
layout: page
title: common/stat (हिन्दी)
description: "फ़ाइल और फ़ाइल सिस्टम की जानकारी दिखाएँ।"
content_hash: 0d6c5dcfdca0f6a30e28ef6560b52ee13e192be4
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

फ़ाइल और फ़ाइल सिस्टम की जानकारी दिखाएँ।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>।

- एक विशिष्ट फ़ाइल के गुण दिखाएँ जैसे आकार, अनुमतियाँ, निर्माण और पहुँच तिथियाँ आदि:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक विशिष्ट फ़ाइल के गुण दिखाएँ जैसे आकार, अनुमतियाँ, निर्माण और पहुँच तिथियाँ आदि बिना लेबल के:

`stat --terse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- उस फ़ाइल सिस्टम की जानकारी दिखाएँ जहाँ एक विशिष्ट फ़ाइल स्थित है:

`stat --file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- केवल ऑक्टल फ़ाइल अनुमतियाँ दिखाएँ:

`stat --format="%a %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक विशिष्ट फ़ाइल का मालिक और समूह दिखाएँ:

`stat --format="%U %G" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक विशिष्ट फ़ाइल का आकार बाइट्स में दिखाएँ:

`stat --format="%s %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>
