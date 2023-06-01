---
layout: page
title: common/cargo-add (தமிழ்)
description: "ரஸ்ட் திட்டத்தின் `Cargo.toml` கோப்பில் சார்புகளைச் சேர்க்கவும்."
content_hash: f97702630fddcd018689c5800fa91f7c25206f48
last_modified_at: 2023-05-28
related_topics:
  - title: English version
    url: /en/common/cargo-add.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo add

ரஸ்ட் திட்டத்தின் `Cargo.toml` கோப்பில் சார்புகளைச் சேர்க்கவும்.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- தற்போதைய திட்டப்பணியில் சார்புநிலையின் சமீபத்திய பதிப்பைச் சேர்க்கவும்:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சார்பு</span>

- சார்புநிலையின் குறிப்பிட்ட பதிப்பைச் சேர்க்கவும்:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சார்பு</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பதிப்பு</span>

- சார்புநிலையைச் சேர்த்து ஒன்று அல்லது அதற்கு மேற்பட்ட குறிப்பிட்ட அம்சங்களை இயக்கவும்:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சார்பு</span>` --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அம்சம்_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அம்சம்_2</span>

- விருப்ப சார்புநிலையைச் சேர்க்கவும், அது கிரேட்டின் அம்சமாக வெளிப்படும்:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சார்பு</span>` --optional`

- சார்புநிலையாக உள்ளூர் கிரேட்டைச் சேர்க்கவும்:

`cargo add --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கிரேட்</span>

- ஒரு மேம்பாட்டைச் சேர்க்கவும் அல்லது சார்புநிலையை உருவாக்கவும்:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சார்பு</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>

- அனைத்து இயல்புநிலை அம்சங்களும் முடக்கப்பட்டுள்ள சார்புநிலையைச் சேர்க்கவும்:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சார்பு</span>` --no-default-features`