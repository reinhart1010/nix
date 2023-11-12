---
layout: page
title: common/rustc (தமிழ்)
description: "ரஸ்ட் கம்பைலர்."
content_hash: b3032614a5240fac0f178075328882aaac096430
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rustc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rustc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustc

ரஸ்ட் கம்பைலர்.
ரஸ்ட் மொழி மூல கோப்புகளை செயலாக்குகிறது, தொகுக்கிறது மற்றும் இணைக்கிறது.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/rustc>.

- ஒரு கோப்பை தொகுக்கவும்:

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.rs</span>

- உயர் தேர்வுமுறையுடன் தொகுக்கவும்:

`rustc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.rs</span>

- பிழைத்திருத்த தகவலுடன் தொகுக்கவும்:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.rs</span>

- தற்போதைய CPU க்கான கட்டிடக்கலை-குறிப்பிட்ட மேம்படுத்தல்களுடன் தொகுக்கவும்:

`rustc -C target-cpu=native `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.rs</span>

- தற்போதைய CPU க்கான கட்டிடக்கலை-குறிப்பிட்ட மேம்படுத்தல்களைக் காண்பி:

`rustc -C target-cpu=native --print cfg`

- இலக்கு பட்டியலைக் காட்டு:

`rustc --print target-list`

- ஒரு குறிப்பிட்ட இலக்கை தொகுக்கவும்:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இலக்கு_மூன்று</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.rs</span>
