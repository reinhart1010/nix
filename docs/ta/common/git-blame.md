---
layout: page
title: common/git-blame (தமிழ்)
description: "ஒரு கோப்பின் ஒவ்வொரு வரியிலும் கமிட் ஹாஷ் மற்றும் கடைசி எழுத்தாளரைக் காட்டு."
content_hash: c8cd9a79b147afccd0f4b970cf282f0e7b133f95
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-blame.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-blame.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-blame.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-blame.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-blame.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-blame.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-blame.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git blame

ஒரு கோப்பின் ஒவ்வொரு வரியிலும் கமிட் ஹாஷ் மற்றும் கடைசி எழுத்தாளரைக் காட்டு.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-blame>.

- ஆசிரியர் பெயருடன் கோப்பை அச்சிட்டு ஒவ்வொரு வரியிலும் ஹாஷ் செய்யுங்கள்:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஆசிரியர் மின்னஞ்சலுடன் கோப்பை அச்சிட்டு ஒவ்வொரு வரியிலும் ஹாஷ் செய்யுங்கள்:

`git blame -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஆசிரியர் பெயருடன் கோப்பை அச்சிடவும் மற்றும் ஒவ்வொரு வரியிலும் ஒரு குறிப்பிட்ட கமிட்டில் ஹாஷ் கமிட் செய்யவும்:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஆசிரியர் பெயருடன் கோப்பை அச்சிட்டு, ஒரு குறிப்பிட்ட உறுதிப்பாட்டிற்கு முன் ஒவ்வொரு வரியிலும் ஹாஷ் செய்யுங்கள்:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்</span>`~ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>
