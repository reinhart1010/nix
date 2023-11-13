---
layout: page
title: common/rustfmt (தமிழ்)
description: "ரஸ்ட் மூலக் குறியீட்டை வடிவமைப்பதற்கான கருவி."
content_hash: af0fa7afd8c84c26bae046d5ba48ea4c1995a01c
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/rustfmt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rustfmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustfmt

ரஸ்ட் மூலக் குறியீட்டை வடிவமைப்பதற்கான கருவி.
மேலும் விவரத்திற்கு: <https://github.com/rust-lang/rustfmt>.

- ஒரு கோப்பை வடிவமைக்கவும், அசல் கோப்பை மேலெழுதவும்:

`rustfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.rs/பாதை</span>

- வடிவமைப்பிற்கான கோப்பைச் சரிபார்த்து, கன்சோலில் ஏதேனும் மாற்றங்களைக் காட்டவும்:

`rustfmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.rs/பாதை</span>

- வடிவமைப்பிற்கு முன் ஏதேனும் மாற்றப்பட்ட கோப்புகளை காப்புப் பிரதி எடுக்கவும் (அசல் கோப்பு `.bk` நீட்டிப்புடன் மறுபெயரிடப்பட்டது):

`rustfmt --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.rs/பாதை</span>
