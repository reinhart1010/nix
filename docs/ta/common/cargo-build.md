---
layout: page
title: common/cargo-build (தமிழ்)
description: "ஒரு உள்ளூர் தொகுப்பு மற்றும் அதன் அனைத்து சார்புகளையும் தொகுக்கவும்."
content_hash: e593393a658e5a47f7babc100555d1f962e8b53e
last_modified_at: 2023-05-28
related_topics:
  - title: English version
    url: /en/common/cargo-build.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo build

ஒரு உள்ளூர் தொகுப்பு மற்றும் அதன் அனைத்து சார்புகளையும் தொகுக்கவும்.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- உள்ளூர் பாதையில் `Cargo.toml` மேனிஃபெஸ்ட் கோப்பால் வரையறுக்கப்பட்ட தொகுப்பு அல்லது தொகுப்புகளை உருவாக்கவும்:

`cargo build`

- மேம்படுத்தல்களுடன், வெளியீட்டு பயன்முறையில் கலைப்பொருட்களை உருவாக்கவும்:

`cargo build --release`

- `Cargo.lock` புதுப்பித்த நிலையில் இருக்க வேண்டும்:

`cargo build --locked`

- பணியிடத்தில் அனைத்து தொகுப்புகளையும் உருவாக்கவும்:

`cargo build --workspace`

- ஒரு குறிப்பிட்ட தொகுப்பை உருவாக்கவும்:

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- குறிப்பிட்ட பைனரியை மட்டும் உருவாக்கவும்:

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

- குறிப்பிட்ட சோதனை இலக்கை மட்டும் உருவாக்கவும்:

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சோதனை_பெயர்</span>
