---
layout: page
title: common/powershell (தமிழ்)
description: "குறிப்பாக கணினி நிர்வாகத்திற்காக வடிவமைக்கப்பட்ட கட்டளை வரி ஷெல் மற்றும் ஸ்கிரிப்டிங் மொழி."
content_hash: a4f94bad3dc3c052be7a914aa397e37c11209280
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/powershell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/powershell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/powershell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/powershell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# powershell

குறிப்பாக கணினி நிர்வாகத்திற்காக வடிவமைக்கப்பட்ட கட்டளை வரி ஷெல் மற்றும் ஸ்கிரிப்டிங் மொழி.
மேலும் பார்க்கவும்: `pwsh`.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- ஊடாடும் ஷெல் அமர்வைத் தொடங்கவும்:

`powershell`

- தொடக்க கட்டமைப்புகளை ஏற்றாமல் ஊடாடும் ஷெல் அமர்வைத் தொடங்கவும்:

`powershell -NoProfile`

- குறிப்பிட்ட கட்டளைகளை இயக்கவும்:

`powershell -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'பவர்ஷெல் செயல்படுத்தப்படுகிறது'</span>`"`

- ஒரு குறிப்பிட்ட ஸ்கிரிப்டை இயக்கவும்:

`powershell -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஸ்கிரிப்ட்.ps1/பாதை</span>

- பவர்ஷெல்லின் குறிப்பிட்ட பதிப்பைக் கொண்டு அமர்வைத் தொடங்கவும்:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பதிப்பு</span>

- தொடக்க கட்டளைகளை இயக்கிய பிறகு ஷெல் வெளியேறுவதைத் தடுக்கவும்:

`powershell -NoExit`

- பவர்ஷெல்லுக்கு அனுப்பப்பட்ட தரவின் வடிவமைப்பை விவரிக்கவும்:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- பவர்ஷெல்லின் வெளியீடு எவ்வாறு வடிவமைக்கப்படுகிறது என்பதைத் தீர்மானிக்கவும்:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
