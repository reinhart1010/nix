---
layout: page
title: common/git-archive (தமிழ்)
description: "பெயரிடப்பட்ட மரத்திலிருந்து கோப்புகளின் காப்பகத்தை உருவாக்கவும்."
content_hash: 81aa351fec6b68d7306210a73b39e133f0a79b9c
related_topics:
  - title: Deutsch version
    url: /de/common/git-archive.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-archive.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-archive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-archive.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-archive.html
    icon: bi bi-globe
---
# git archive

பெயரிடப்பட்ட மரத்திலிருந்து கோப்புகளின் காப்பகத்தை உருவாக்கவும்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-archive>.

- தற்போதைய HEAD இன் உள்ளடக்கங்களிலிருந்து ஒரு தார் காப்பகத்தை உருவாக்கி அதை நிலையான வெளியீட்டில் அச்சிடுக:

`git archive --verbose HEAD`

- தற்போதைய HEAD இலிருந்து ஒரு ஜிப் காப்பகத்தை உருவாக்கி அதை நிலையான வெளியீட்டில் அச்சிடுக:

`git archive --verbose --format=zip HEAD`

- மேலே உள்ளதைப் போலவே, ஆனால் கோப்புக்கு ஜிப் காப்பகத்தை எழுதவும்:

`git archive --verbose --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை/கோப்பு.zip</span>` HEAD`

- ஒரு குறிப்பிட்ட கிளையில் சமீபத்திய உறுதிப்பாட்டின் உள்ளடக்கங்களிலிருந்து தார் காப்பகத்தை உருவாக்கவும்:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை/கோப்பு.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளை_பெயர்</span>

- ஒரு குறிப்பிட்ட கோப்பகத்தின் உள்ளடக்கங்களிலிருந்து தார் காப்பகத்தை உருவாக்கவும்:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை/கோப்பு.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பகத்திற்கான/பாதை</span>

- ஒவ்வொரு கோப்பிற்கும் ஒரு குறிப்பிட்ட கோப்பகத்திற்குள் காப்பகப்படுத்த ஒரு பாதையைத் தயாரிக்கவும்:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை/கோப்பு.tar</span>` --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தயார்படுத்தும்/பாதை</span>`/ HEAD`
