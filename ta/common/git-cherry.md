---
layout: page
title: common/git-cherry (தமிழ்)
description: "அப்ஸ்ட்ரீமில் இன்னும் பயன்படுத்தப்படாத கமிட்டுகளைக் கண்டறியவும்."
content_hash: 3823b7cf8da6f0b2d07353367f3d3426ee7e627e
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
---
# git cherry

அப்ஸ்ட்ரீமில் இன்னும் பயன்படுத்தப்படாத கமிட்டுகளைக் கண்டறியவும்.
மேலும் தகவல்: <https://git-scm.com/docs/git-cherry>.

- அப்ஸ்ட்ரீமில் சமமான கமிட்டுகளுடன் கமிட்டுகளையும் (அவற்றின் செய்திகளையும்) காட்டு:

`git cherry -v`

- வேறு அப்ஸ்ட்ரீம் மற்றும் தலைப்பு கிளையை குறிப்பிடவும்:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தோற்றம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தலைப்பு</span>

- கொடுக்கப்பட்ட வரம்புக்குள் கமிட்களை கட்டுப்படுத்து:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தோற்றம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தலைப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடித்தளம்</span>
