---
layout: page
title: common/git-bisect (தமிழ்)
description: "ஒரு பிழையை அறிமுகப்படுத்திய உறுதிப்பாட்டைக் கண்டுபிடிக்க பைனரி தேடலைப் பயன்படுத்தவும்."
content_hash: ad0790595641f7fcd8babf7438b50ba1fb11acf1
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bisect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bisect.html
    icon: bi bi-globe
---
# git bisect

ஒரு பிழையை அறிமுகப்படுத்திய உறுதிப்பாட்டைக் கண்டுபிடிக்க பைனரி தேடலைப் பயன்படுத்தவும்.
தவறான உறுதிப்பாட்டை படிப்படியாகக் குறைக்க கிட் தானாகவே கமிட் வரைபடத்தில் முன்னும் பின்னுமாக குதிக்கிறது.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-bisect>.

- அறியப்பட்ட தரமற்ற கமிட் மற்றும் அறியப்பட்ட சுத்தமான (பொதுவாக பழையது) வரம்புக்குட்பட்ட ஒரு கமிட் வரம்பில் ஒரு இரு அமர்வு தொடங்கவும்:

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மோசமான_கமிட்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நல்ல_கமிட்</span>

- `git bisect` தேர்ந்தெடுக்கும் ஒவ்வொரு உறுதிப்பாட்டிற்கும், சிக்கலுக்காக அதைச் சோதித்தபின் அதை" கெட்டது "அல்லது" நல்லது "என்று குறிக்கவும்:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- `git bisect` தவறான செயலை சுட்டிக்காட்டிய பின், இருசக்கர அமர்வை முடித்துவிட்டு முந்தைய கிளைக்குத் திரும்புக:

`git bisect reset`

- ஒரு பிரிவின் போது ஒரு உறுதிப்பாட்டைத் தவிர்க்கவும் (எ.கா. வேறுபட்ட பிரச்சினை காரணமாக சோதனைகளில் தோல்வியுற்றது):

`git bisect skip`
