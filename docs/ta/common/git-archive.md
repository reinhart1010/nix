---
layout: page
title: common/git-archive (தமிழ்)
description: "பெயரிடப்பட்ட மரத்திலிருந்து கோப்புகளின் காப்பகத்தை உருவாக்கவும்."
content_hash: 12123ab693cfc0667f15d67a0368a33d55210935
last_modified_at: 2024-09-30
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
  - title: Indonesia version
    url: /id/common/git-archive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-archive.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-archive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git archive

பெயரிடப்பட்ட மரத்திலிருந்து கோப்புகளின் காப்பகத்தை உருவாக்கவும்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-archive>.

- தற்போதைய HEAD இன் உள்ளடக்கங்களிலிருந்து ஒரு தார் காப்பகத்தை உருவாக்கி அதை நிலையான வெளியீட்டில் அச்சிடுக:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` HEAD`

- தற்போதைய HEAD இலிருந்து ஒரு ஜிப் காப்பகத்தை உருவாக்கி அதை நிலையான வெளியீட்டில் அச்சிடுக:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` --format zip HEAD`

- மேலே உள்ளதைப் போலவே, ஆனால் கோப்புக்கு ஜிப் காப்பகத்தை எழுதவும்:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.zip/பாதை</span>` HEAD`

- ஒரு குறிப்பிட்ட கிளையில் சமீபத்திய உறுதிப்பாட்டின் உள்ளடக்கங்களிலிருந்து தார் காப்பகத்தை உருவாக்கவும்:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.tar/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளை_பெயர்</span>

- ஒரு குறிப்பிட்ட கோப்பகத்தின் உள்ளடக்கங்களிலிருந்து தார் காப்பகத்தை உருவாக்கவும்:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.tar/பாதை</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>

- ஒவ்வொரு கோப்பிற்கும் ஒரு குறிப்பிட்ட கோப்பகத்திற்குள் காப்பகப்படுத்த ஒரு பாதையைத் தயாரிக்கவும்:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.tar/பாதை</span>` --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தயார்படுத்தும்/பாதை</span>`/ HEAD`
