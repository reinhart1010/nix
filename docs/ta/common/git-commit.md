---
layout: page
title: common/git-commit (தமிழ்)
description: "கோப்புகளை களஞ்சியத்திற்கு கமிட்செய்ய."
content_hash: 3e6d03066c9dd323256f8d4bfb3b05d2e3da843a
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
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
---
# git commit

கோப்புகளை களஞ்சியத்திற்கு கமிட்செய்ய.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-commit>.

- ஒரு செய்தியுடன் களஞ்சியத்திற்கு அரங்குக் கோப்புகளை கமிட் செய்யுங்கள்:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- ஒரு கோப்பிலிருந்து படிக்கப்பட்ட செய்தியுடன் கட்டப்பட்ட கோப்புகளை கமிட்செய்யவும்:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கமிட்_செய்தி_கோப்பு</span>

- அனைத்து மாற்றியமைக்கப்பட்ட கோப்புகளையும் தானாக நிலைநிறுத்து, செய்தியுடன் கமிட் செய்யுங்கள்:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- ஸ்டேஜ் செய்யப்பட்ட கோப்புகளை கமிட்செய்து, அவற்றை `~/.gitconfig` இல் வரையறுக்கப்பட்ட GPG விசையுடன் [S] கையொப்பமிடுங்கள்:

`git commit -S -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- கடைசி கட்டத்தை தற்போதைய நிலை மாற்றங்களுடன் கமிட் செய்யுங்கள்:

`git commit --amend`

- குறிப்பிட்ட (ஏற்கனவே அரங்கேற்றப்பட்ட) கோப்புகளை மட்டுமே கமிட் செய்யுங்கள்:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு2</span>

- கட்டப்பட்ட கோப்புகள் இல்லாவிட்டாலும், கமிட்டை உருவாக்கவும்:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`" --allow-empty`
