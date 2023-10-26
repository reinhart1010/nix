---
layout: page
title: common/a2ping (हिन्दी)
description: "छवियों को ईपीएस या पीडीएफ फाइलों में परिवर्तित करें।"
content_hash: 86f3ea3f2e1706e3ccb3745e76acc31512d40b71
last_modified_at: 2023-10-26
related_topics:
  - title: English version
    url: /en/common/a2ping.html
    icon: bi bi-globe
---
# a2ping

छवियों को ईपीएस या पीडीएफ फाइलों में परिवर्तित करें।
अधिक जानकारी: <https://manned.org/a2ping>.

- एक छवि को पीडीएफ में बदलें (ध्यान दें: आउटपुट फ़ाइल नाम निर्दिष्ट करना वैकल्पिक है):

`a2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/छवि.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>

- निर्दिष्ट विधि का उपयोग करके दस्तावेज़ को संपीड़ित करें:

`a2ping --nocompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|zip|best|flate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फ़ाइल</span>

- यदि मौजूद है तो HiResBoundingBox को स्कैन करें (ध्यान दें: यह डिफ़ॉल्ट रूप से हाँ है):

`a2ping --nohires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फ़ाइल</span>

- मूल पृष्ठ के नीचे और बाईं ओर पृष्ठ सामग्री की अनुमति दें (नोट: यह डिफ़ॉल्ट रूप से नहीं है):

`a2ping --below `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फ़ाइल</span>

- `gs` के लिए अतिरिक्त तर्क पारित करें:

`a2ping --gsextra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">तर्क</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फ़ाइल</span>

- बाहरी प्रोग्राम में अतिरिक्त तर्क पास करें (यानी पीडीएफटॉप्स):

`a2ping --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">तर्क</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फ़ाइल</span>

- सहायता प्रदर्शित करें:

`a2ping -h`
