---
layout: page
title: common/rustc (தமிழ்)
description: "ரஸ்ட் கம்பைலர்."
content_hash: 437ca96334944c3d845ca9d69d1a8e753753f1d8
last_modified_at: 2023-11-13
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

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய_கோப்பு.rs/பாதை</span>

- உகப்பாக்கத்துடன் தொகுக்கவும் (`s` என்பது பைனரி அளவுக்கு உகந்ததாக்கு; `z` என்பது இன்னும் கூடுதலான மேம்படுத்தலுடன் சமம்):

`rustc -C lto -C opt-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3|s|z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய_கோப்பு.rs/பாதை</span>

- பிழைத்திருத்த தகவலுடன் தொகுக்கவும்:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய_கோப்பு.rs/பாதை</span>

- ஒரு பிழை செய்தியை விளக்குங்கள்:

`rustc --explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பிழை_குறியீடு</span>

- தற்போதைய CPU க்கான கட்டிடக்கலை-குறிப்பிட்ட மேம்படுத்தல்களுடன் தொகுக்கவும்:

`rustc -C target-cpu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">native</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய_கோப்பு.rs/பாதை</span>

- இலக்கு பட்டியலைக் காண்பி (குறிப்பு: `rustup` ஐப் பயன்படுத்தி ஒரு இலக்கை முதலில் தொகுக்க நீங்கள் சேர்க்க வேண்டும்):

`rustc --print target-list`

- ஒரு குறிப்பிட்ட இலக்கை தொகுக்கவும்:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இலக்கு_மூன்று</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய_கோப்பு.rs/பாதை</span>
