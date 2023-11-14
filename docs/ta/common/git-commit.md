---
layout: page
title: common/git-commit (தமிழ்)
description: "கோப்புகளை களஞ்சியத்திற்கு கமிட்செய்ய."
content_hash: f2b2f59b7f8cb60033241695d68a541c7b6ddb0c
last_modified_at: 2023-11-14
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit

கோப்புகளை களஞ்சியத்திற்கு கமிட்செய்ய.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-commit>.

- ஒரு செய்தியுடன் களஞ்சியத்திற்கு அரங்குக் கோப்புகளை கமிட் செய்யுங்கள்:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- ஒரு கோப்பிலிருந்து படிக்கப்பட்ட செய்தியுடன் கட்டப்பட்ட கோப்புகளை கமிட்செய்யவும்:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கமிட்_செய்தி_கோப்பு/பாதை</span>

- அனைத்து மாற்றியமைக்கப்பட்ட கோப்புகளையும் தானாக நிலைநிறுத்து, செய்தியுடன் கமிட் செய்யுங்கள்:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- ஸ்டேஜ் செய்யப்பட்ட கோப்புகளை உறுதிசெய்து, குறிப்பிட்ட GPG விசையுடன் கையொப்பமிடுங்கள் (அல்லது எந்த வாதமும் குறிப்பிடப்படவில்லை எனில் கட்டமைப்பு கோப்பில் வரையறுக்கப்பட்ட ஒன்று):

`git commit --gpg-sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>` --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- தற்போது செய்யப்பட்ட மாற்றங்களைச் சேர்ப்பதன் மூலம் கடைசி கமிட்டைப் புதுப்பிக்கவும், கமிட் இன் ஹாஷை மாற்றவும்:

`git commit --amend`

- குறிப்பிட்ட (ஏற்கனவே அரங்கேற்றப்பட்ட) கோப்புகளை மட்டுமே கமிட் செய்யுங்கள்:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2/பாதை</span>

- கட்டப்பட்ட கோப்புகள் இல்லாவிட்டாலும், கமிட்டை உருவாக்கவும்:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`" --allow-empty`
