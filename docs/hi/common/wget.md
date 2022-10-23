---
layout: page
title: common/wget (हिन्दी)
description: "वेब से फ़ाइलें डाउनलोड करें।"
content_hash: cff9822554c4c74c1a8d23e157eddb75cdee6abd
related_topics:
  - title: English version
    url: /en/common/wget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/wget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wget.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wget

वेब से फ़ाइलें डाउनलोड करें।
HTTP, HTTPS और FTP का समर्थन करता है।
अधिक जानकारी: <https://www.gnu.org/software/wget>.

- किसी फ़ाइल में URL की अंतर्वस्तु डाउनलोड करें (इस मामले में "foo" नाम दिया गया है):

`wget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- किसी फ़ाइल में URL की अंतर्वस्तु डाउनलोड करें (इस मामले में "bar" नाम दिया गया है):

`wget --output-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- अनुरोधों के बीच 3-सेकंड अंतराल के साथ एक एकल वेब पेज और उसके सभी संसाधन डाउनलोड करें (स्क्रिप्ट्स, स्टाइलशीट, चित्र, आदि।):

`wget --page-requisites --convert-links --wait=3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepage.html</span>

- एक निर्देशिका और उसकी उप-निर्देशिकाओं में सभी सूचीबद्ध फ़ाइलें डाउनलोड करें (अंतर्निहित पृष्ठ तत्व डाउनलोड नहीं करता):

`wget --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- डाउनलोड की गति और कनेक्शन के पुन: प्रयास की संख्या सीमित करें:

`wget --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- मूल प्रमाणीकरण का उपयोग करके किसी HTTP सर्वर से फ़ाइल डाउनलोड करें (FTP के लिए भी काम करता है):

`wget --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पासवर्ड</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- अधूरा डाउनलोड जारी रखें:

`wget --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- टेक्स्ट फ़ाइल में संग्रहीत सभी URL को एक विशिष्ट निर्देशिका में डाउनलोड करें:

`wget --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URLs.txt</span>
