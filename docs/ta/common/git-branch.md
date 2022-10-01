---
layout: page
title: common/git-branch (தமிழ்)
description: "கிளைகளுடன் வேலை செய்வதற்கான பிரதான கிட் கட்டளை."
content_hash: 6aab5055315b215709e5acec6855a2be6ab43a57
related_topics:
  - title: Deutsch version
    url: /de/common/git-branch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-branch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-branch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-branch.html
    icon: bi bi-globe
---
# git branch

கிளைகளுடன் வேலை செய்வதற்கான பிரதான கிட் கட்டளை.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-branch>.

- அனைத்து கிளைகளையும் பட்டியலிடுங்கள் (உள்ளூர் மற்றும் தொலைதூர; தற்போதைய கிளை `*` மூலம் சிறப்பிக்கப்படுகிறது):

`git branch --all`

- எந்தெந்த கிளைகள் தங்கள் வரலாற்றில் குறிப்பிட்ட Git கமிட்டை உள்ளடக்கியிருக்கின்றன என்பதை பட்டியலிடுங்கள்:

`git branch --all --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்_ஹாஷ்</span>

- தற்போதைய கிளையின் பெயரைக் காட்டு:

`git branch --show-current`

- தற்போதைய கமிட்டின் அடிப்படையில் புதிய கிளையை உருவாக்கவும்:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>

- ஒரு குறிப்பிட்ட கமிட்டின் அடிப்படையில் புதிய கிளையை உருவாக்கவும்:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்_ஹாஷ்</span>

- ஒரு கிளையின் மறுபெயரிடு (இதை செய்ய அந்த கிளையை செக்கவுட் செய்த்திருக்க கூடாது):

`git branch -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பழைய_கிளையின்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">புதிய_கிளையின்_பெயர்</span>

- கணினியில் ஒரு கிளையை நீக்கு (இதை செய்ய அந்த கிளையை செக்கவுட் செய்த்திருக்க கூடாது):

`git branch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>

- தொலை களஞ்சியத்தில் ஒரு கிளையை நீக்கு:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_பெயர்</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_கிளையின்_பெயர்</span>
