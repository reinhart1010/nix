---
layout: page
title: common/git-blame (தமிழ்)
description: "ஒரு கோப்பின் ஒவ்வொரு வரியிலும் கமிட் ஹாஷ் மற்றும் கடைசி எழுத்தாளரைக் காட்டு."
content_hash: 11e1aa9154837a418254e037aecf6a93e41f2bb2
last_modified_at: 2025-03-02
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
  - title: Indonesia version
    url: /id/common/git-blame.html
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
  - title: українська version
    url: /uk/common/git-blame.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git blame

ஒரு கோப்பின் ஒவ்வொரு வரியிலும் கமிட் ஹாஷ் மற்றும் கடைசி எழுத்தாளரைக் காட்டு.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-blame>.

- ஆசிரியர் பெயருடன் கோப்பை அச்சிட்டு ஒவ்வொரு வரியிலும் ஹாஷ் செய்யுங்கள்:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- ஆசிரியர் மின்னஞ்சலுடன் கோப்பை அச்சிட்டு ஒவ்வொரு வரியிலும் ஹாஷ் செய்யுங்கள்:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--show-email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- ஆசிரியர் பெயருடன் கோப்பை அச்சிடவும் மற்றும் ஒவ்வொரு வரியிலும் ஒரு குறிப்பிட்ட கமிட்டில் ஹாஷ் கமிட் செய்யவும்:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- ஆசிரியர் பெயருடன் கோப்பை அச்சிட்டு, ஒரு குறிப்பிட்ட உறுதிப்பாட்டிற்கு முன் ஒவ்வொரு வரியிலும் ஹாஷ் செய்யுங்கள்:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்</span>`~ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>
