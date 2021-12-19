---
layout: page
title: common/ln (हिन्दी)
description: "फाइलों और निर्देशिकाओं के लिंक बनाता है।"
content_hash: aa554167f9195d8f87d5ab8ce45397b28f5cccfe
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
---
# ln

फाइलों और निर्देशिकाओं के लिंक बनाता है।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/ln>।

- किसी फ़ाइल या निर्देशिका के लिए एक प्रतीकात्मक लिंक बनाएँ:

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/फ़ाइल_या_निर्देशिका/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लिंक/का/पथ</span>

- किसी भिन्न फ़ाइल को इंगित करने के लिए मौजूदा प्रतीकात्मक लिंक को अधिलेखित करें:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/नई_फ़ाइल/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लिंक/का/पथ</span>

- किसी फ़ाइल का हार्ड लिंक बनाएँ:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/फ़ाइल/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">हार्डलिंक/का/पथ</span>
