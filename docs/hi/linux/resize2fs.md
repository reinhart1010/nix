---
layout: page
title: linux/resize2fs (हिन्दी)
description: "ext2, ext3 या ext4 फाइल सिस्टम का आकार बदलें।"
content_hash: 0c193d2bdfdfa959322e19e9c39226235f88d268
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/linux/resize2fs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# resize2fs

ext2, ext3 या ext4 फाइल सिस्टम का आकार बदलें।
यह अंतर्निहित पार्टीशन का आकार नहीं बदलता है। फाइल सिस्टम को पहले अनमाउंट करना पड़ सकता है, अधिक जानकारी के लिए मैन पेज पढ़ें।
अधिक जानकारी: <https://manned.org/resize2fs>।

- स्वचालित रूप से फाइल सिस्टम का आकार बदलें:

`resize2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 40G के आकार में फाइल सिस्टम का आकार बदलें, प्रगति बार दिखाते हुए:

`resize2fs -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40G</span>

- फाइल सिस्टम को उसके न्यूनतम संभव आकार में सिकोड़ें:

`resize2fs -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
