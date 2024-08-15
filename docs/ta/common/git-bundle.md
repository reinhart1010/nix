---
layout: page
title: common/git-bundle (தமிழ்)
description: "ஒரு காப்பக கோப்பில் பொருள்கள் மற்றும் குறிப்புகளை தொகுக்கவும்."
content_hash: b075455a139fea61aeb0b0356e266709c10efcb5
last_modified_at: 2024-08-15
related_topics:
  - title: English version
    url: /en/common/git-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bundle.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bundle.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git bundle

ஒரு காப்பக கோப்பில் பொருள்கள் மற்றும் குறிப்புகளை தொகுக்கவும்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-bundle>.

- ஒரு குறிப்பிட்ட கிளையின் அனைத்து பொருள்கள் மற்றும் குறிப்புகளைக் கொண்ட ஒரு மூட்டை கோப்பை உருவாக்கவும்:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.bundle/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>

- அனைத்து கிளைகளின் மூட்டை கோப்பை உருவாக்கவும்:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.bundle/பாதை</span>` --all`

- தற்போதைய கிளையின் கடைசி 5 கமிட்டுகளின் மூட்டை கோப்பை உருவாக்கவும்:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.bundle/பாதை</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- சமீபத்திய 7 நாட்களின் மூட்டை கோப்பை உருவாக்கவும்:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.bundle/பாதை</span>` --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.days</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- ஒரு மூட்டை கோப்பு தற்போதைய களஞ்சியத்தில் செல்லுபடியாகும் மற்றும் பயன்படுத்தலாம் என்பதை சரிபார்க்கவும்:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.bundle/பாதை</span>

- ஒரு மூட்டையில் உள்ள குறிப்புகளின் பட்டியலை நிலையான வெளியீட்டில் அச்சிடுக:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.bundle/பாதை</span>

- ஒரு மூட்டை கோப்பிலிருந்து ஒரு குறிப்பிட்ட கிளையை தற்போதைய களஞ்சியத்தில் இணைக்கவும்:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.bundle/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>
