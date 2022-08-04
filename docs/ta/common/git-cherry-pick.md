---
layout: page
title: common/git-cherry-pick (தமிழ்)
description: "தற்போதுள்ள கமிட்டுகளால் அறிமுகப்படுத்தப்பட்ட மாற்றங்களை தற்போதைய கிளையில் பயன்படுத்துங்கள்."
content_hash: 5256ab88ef9b34566b85fd38f283bce765ced0ea
related_topics:
  - title: বাংলা version
    url: /bn/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry-pick.html
    icon: bi bi-globe
---
# git cherry-pick

தற்போதுள்ள கமிட்டுகளால் அறிமுகப்படுத்தப்பட்ட மாற்றங்களை தற்போதைய கிளையில் பயன்படுத்துங்கள்.
மற்றொரு கிளையில் மாற்றங்களைப் பயன்படுத்த, முதலில் விரும்பிய கிளைக்கு மாற `git checkout` ஐப் பயன்படுத்தவும்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-cherry-pick>.

- தற்போதைய கிளைக்கு ஒரு கமிட்டை பயன்படுத்துங்கள்:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்</span>

- தற்போதைய கிளையில் பலவிதமான கமிட்டுகளைப் பயன்படுத்துங்கள் (மேலும் `git rebase --onto` பார்க்கவும் ):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொடக்க_கமிட்</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முடிவு_கமிட்</span>

- தற்போதைய கிளைக்கு பல (வரிசை அல்லாத) கமிட்டுகளைப் பயன்படுத்துங்கள்:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்_2</span>

- ஒரு கமிட்டை உருவாக்காமல், பணிபுரியும் கோப்பகத்தில் ஒரு கமிட்டின் மாற்றங்களைச் சேர்க்கவும்:

`git cherry-pick -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்</span>
