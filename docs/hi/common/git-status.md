---
layout: page
title: common/git-status (हिन्दी)
description: "गिट रिपॉजिटरी में फाइलों में बदलाव दिखाएं।"
content_hash: 293b7ffb6c900542ce920f91ffbd65369841386a
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-status.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-status.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
---
# git status

गिट रिपॉजिटरी में फाइलों में बदलाव दिखाएं।
उन पथों को प्रदर्शित करता है जिनमें अनुक्रमणिका फ़ाइल और वर्तमान हेड कमिट के बीच अंतर होता है।
अधिक जानकारी: <https://git-scm.com/docs/git-status>।

- बदली हुई फ़ाइलें दिखाएं जो अभी तक कमिट के लिए नहीं जोड़ी गई हैं:

`git status`

- शॉर्ट-फॉर्मेट में आउटपुट दें:

`git status -s`

- आउटपुट में ट्रैक न की गई फ़ाइलें न दिखाएं:

`git status --untracked-files=no`

- [b]शाखा की जानकारी के साथ [s]लघु प्रारूप में आउटपुट दिखाएं:

`git status -sb`
