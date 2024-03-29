---
layout: page
title: common/rustup (தமிழ்)
description: "ரஸ்ட் டூல்செயின் நிறுவி."
content_hash: 8641454b05a4312bd9dbd8f8ad1d91fdaa63c6a6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rustup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustup

ரஸ்ட் டூல்செயின் நிறுவி.
ரஸ்ட் டூல்செயின்களை நிறுவவும், நிர்வகிக்கவும் மற்றும் புதுப்பிக்கவும் இதை பயன்படுத்துகிறோம்.
மேலும் விவரத்திற்கு: <https://rust-lang.github.io/rustup>.

- உங்கள் கணினிக்கு இரவு டூல்செயின்களை நிறுவவும்:

`rustup install nightly`

- இயல்புநிலை டூல்செயின்களை இரவிற்கு மாற்றவும், இதனால் `cargo` மற்றும் `rustc` கட்டளைகள் அதைப் பயன்படுத்தும்:

`rustup default nightly`

- தற்போதைய ப்ராஜெக்ட்டில் இருக்கும் போது இரவு டூல்செயினைப் பயன்படுத்தவும், ஆனால் உலகளாவிய அமைப்புகளை மாற்றாமல் விடவும்:

`rustup override set nightly`

- அனைத்து டூல்செயின்களையும் புதுப்பிக்கவும்:

`rustup update`

- நிறுவப்பட்ட டூல்செயின்களை பட்டியலிடுங்கள்:

`rustup show`

- ஒரு குறிப்பிட்ட டூல்செயின் மூலம் சரக்கு கட்டமைப்பை இயக்கவும்:

`rustup run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">டூல்செயின்_பெயர்</span>` cargo build`

- இயல்புநிலை இணைய உலாவியில் உள்ளூர் ரஸ்ட் ஆவணத்தைத் திறக்கவும்:

`rustup doc`
