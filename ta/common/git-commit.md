---
layout: page
title: common/git-commit (தமிழ்)
description: "கோப்புகளை களஞ்சியத்திற்கு கமிட்செய்ய."
content_hash: a9c237983fa1741a623be2f8e2d756baacf43b42
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
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-commit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git commit

கோப்புகளை களஞ்சியத்திற்கு கமிட்செய்ய.
மேலும் தகவல்: <https://git-scm.com/docs/git-commit>.

- ஒரு செய்தியுடன் களஞ்சியத்திற்கு அரங்குக் கோப்புகளை கமிட் செய்யுங்கள்:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- அனைத்து மாற்றியமைக்கப்பட்ட கோப்புகளையும் தானாக நிலைநிறுத்து, செய்தியுடன் கமிட் செய்யுங்கள்:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- கடைசி கட்டத்தை தற்போதைய நிலை மாற்றங்களுடன் கமிட் செய்யுங்கள்:

`git commit --amend`

- குறிப்பிட்ட (ஏற்கனவே அரங்கேற்றப்பட்ட) கோப்புகளை மட்டுமே கமிட் செய்யுங்கள்:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எனது/கோப்பு1க்கான/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எனது/கோப்பு2க்கான/பாதை</span>
