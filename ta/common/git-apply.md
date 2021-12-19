---
layout: page
title: common/git-apply (தமிழ்)
description: "கோப்புகள் மற்றும் / அல்லது குறியீட்டுக்கு ஒரு இணைப்பு பயன்படுத்தவும்."
content_hash: 103cefe12ad78072567841a7b474a34cf30a0d11
related_topics:
  - title: Deutsch version
    url: /de/common/git-apply.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-apply.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-apply.html
    icon: bi bi-globe
---
# git apply

கோப்புகள் மற்றும் / அல்லது குறியீட்டுக்கு ஒரு இணைப்பு பயன்படுத்தவும்.
மேலும் தகவல்: <https://git-scm.com/docs/git-apply>.

- இணைக்கப்பட்ட கோப்புகளைப் பற்றிய செய்திகளை அச்சிடுங்கள்:

`git apply --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை</span>

- இணைக்கப்பட்ட கோப்புகளை குறியீட்டில் பயன்படுத்தவும் மற்றும் சேர்க்கவும்:

`git apply --index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை</span>

- ரிமோட் பேட்ச் கோப்பைப் பயன்படுத்துங்கள்:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/கோப்பு.patch</span>` | git apply`

- உள்ளீட்டிற்கான வெளியீட்டு வேறுபாடு நிலை மற்றும் இணைப்பு பொருந்தும்:

`git apply --stat --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை</span>

- பேட்சை தலைகீழாகப் பயன்படுத்துங்கள்:

`git apply --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை</span>

- பேட்ச் முடிவை குறியீட்டில் வேலை செய்யும் மரத்தை மாற்றாமல் சேமிக்கவும்:

`git apply --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை</span>
