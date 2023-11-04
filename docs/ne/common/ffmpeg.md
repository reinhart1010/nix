---
layout: page
title: common/ffmpeg (नेपाली)
description: "भिडियो रूपान्तरण उपकरण।"
content_hash: d7498066a08ee8435d0fe97f0bf7c97dc5207556
last_modified_at: 2023-11-04
related_topics:
  - title: Deutsch version
    url: /de/common/ffmpeg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ffmpeg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffmpeg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ffmpeg.html
    icon: bi bi-globe
---
# ffmpeg

भिडियो रूपान्तरण उपकरण।
थप जानकारी: <https://ffmpeg.org>.

- भिडियोबाट ध्वनि निकाल्नुहोस् र MP3 को रूपमा सेभ गर्नुहोस:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">भिडियो.mp4</span>` -vn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ध्वनि</span>`.mp3`

- भिडियोको उचाइ 1000px मा स्केल गर्दै र फ्रेमरेटलाई 15 राखेर GIF को रूपमा सेभ गर्नुहोस:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">भिडियो.mp4</span>` -vf 'scale=-1:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>`' -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट.gif</span>

- अंकित छविहरूलाइ(`फ्रेम_1.jpg`, `फ्रेम_2.jpg`, आदि) भिडियो वा GIF मा जोड्नुहोस:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ्रेम_%d.jpg</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">भिडियो.mpg|भिडियो.gif</span>

- भिडियोको mm:ss बाट एकल फ्रेम निकाल्नुहोस् र यसलाई 128x128 रिजोल्युसनको छविको रूपमा सेभ गर्नुहोस्:

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">भिडियो.mp4</span>` -frames 1 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">128x128</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि.png</span>

- दिइएको सुरु समय mm:ss देखि अन्त्यसमय mm2:ss2 सम्म भिडियोलाइ काट्नुहोस (अन्त्य सम्म नै काट्नलाई -to फ्ल्याग हटाउनुहोस्):

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm2:ss2</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">भिडियो.mp4</span>` -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट.mp4</span>

- AVI भिडियोलाई MP4 मा रूपान्तरण गर्नुहोस्। अडियोको 128kbit बिटरेट राखेर AAC मा, भिडियोको CRF 23 राखेर h264 मा:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_भिडियो</span>`.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_भिडियो</span>`.mp4`

- MKV भिडियोको अडियो वा भिडियो स्ट्रिमहरू पुन: एन्कोडिङ नगरी हानिरहित ढाँचामा MP4 मा बदल्नुहोस:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_भिडियो</span>`.mkv -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_भिडियो</span>`.mp4`

- MP4 भिडियोलाई VP9 कोडेकमा रूपान्तरण गर्नुहोस्। उत्कृष्ट गुणस्तरको लागि, CRF फ्ल्यागको प्रयोग गर्नुहोस् (सिफारिस गरिएको दायरा 15-35) र `-b:video 0` पनि प्रयोग गर्नुहोस्:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_भिडियो</span>`.mp4 -codec:video libvpx-vp9 -crf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -b:video 0 -codec:audio libopus -vbr on -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">थ्रेड_संख्या</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_भिडियो</span>`.webm`
