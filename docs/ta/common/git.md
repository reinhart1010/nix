---
layout: page
title: common/git (தமிழ்)
description: "விநியோகிக்கப்பட்ட பதிப்பு கட்டுப்பாட்டு அமைப்பு."
content_hash: df70ad7b2a0199ae293c97c89ee07b251291860c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/git.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/git.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git

விநியோகிக்கப்பட்ட பதிப்பு கட்டுப்பாட்டு அமைப்பு.
`commit`, `add`, `branch`, `checkout`, `push`போன்ற சில துணைக் கட்டளைகள் அவற்றின் சொந்த பயன்பாட்டு ஆவணங்களைக் கொண்டுள்ளன, அவை `tldr git subcommand` வழியாக அணுகலாம்.
மேலும் விவரத்திற்கு: <https://git-scm.com/>.

- Git பதிப்பைச் சரிபார்க்கவும்:

`git --version`

- பொதுவான உதவியைக் காட்டு:

`git --help`

- Git துணைக் கட்டளையில் உதவியைக் காட்டு (`clone`, `add`, `push`, `log` போன்றவை.):

`git help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">துணை_கட்டளை</span>

- ஒரு Git துணைக் கட்டளையை இயக்கவும்:

`git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">துணை_கட்டளை</span>

- தனிப்பயன் களஞ்சிய வேர் பாதையில் Git துணைக் கட்டளையை இயக்கவும்:

`git -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/களஞ்சியம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">துணை_கட்டளை</span>

- கொடுக்கப்பட்ட உள்ளமைவு தொகுப்புடன் Git துணைக் கட்டளையை இயக்கவும்:

`git -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டமைப்பு.சாவி</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மதிப்பு</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">துணை_கட்டளை</span>
