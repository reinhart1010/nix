---
layout: page
title: common/cargo-test (தமிழ்)
description: "ரஸ்ட் தொகுப்பின் அலகு மற்றும் ஒருங்கிணைப்பு சோதனைகளை செயல்படுத்தவும்."
content_hash: 70f8eb91f9c7209fbfc72bc284e826d05c607ca7
last_modified_at: 2023-05-28
related_topics:
  - title: English version
    url: /en/common/cargo-test.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo test

ரஸ்ட் தொகுப்பின் அலகு மற்றும் ஒருங்கிணைப்பு சோதனைகளை செயல்படுத்தவும்.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- அவர்களின் பெயர்களில் ஒரு குறிப்பிட்ட சரம் உள்ள சோதனைகளை மட்டும் இயக்கவும்:

`cargo test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சோதனை_பெயர்</span>

- ஒரே நேரத்தில் இயங்கும் சோதனை வழக்குகளின் எண்ணிக்கையை அமைக்கவும்:

`cargo test -- --test-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எண்ணிக்கை</span>

- `Cargo.lock` புதுப்பித்த நிலையில் இருக்க வேண்டும்:

`cargo test --locked`

- மேம்படுத்தல்களுடன், வெளியீட்டு பயன்முறையில் கலைப்பொருட்களை சோதிக்கவும்:

`cargo test --release`

- பணியிடத்தில் உள்ள அனைத்து தொகுப்புகளையும் சோதிக்கவும்:

`cargo test --workspace`

- ஒரு தொகுப்புக்கான சோதனைகளை இயக்கவும்:

`cargo test --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- சோதனைச் செயலாக்கங்களிலிருந்து வெளியீட்டை மறைக்காமல் சோதனைகளை இயக்கவும்:

`cargo test -- --nocapture`
