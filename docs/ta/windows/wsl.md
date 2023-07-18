---
layout: page
title: windows/wsl (தமிழ்)
description: "லினக்ஸிற்கான விண்டோஸ் துணை அமைப்பை கட்டளை வரியிலிருந்து நிர்வகிக்கவும்."
content_hash: f2318f36becf8f9693c1a0eeb75b38b9d8ae86dc
last_modified_at: 2023-07-18
related_topics:
  - title: Deutsch version
    url: /de/windows/wsl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/wsl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wsl

லினக்ஸிற்கான விண்டோஸ் துணை அமைப்பை கட்டளை வரியிலிருந்து நிர்வகிக்கவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows/wsl/reference>.

- லினக்ஸ் ஷெல்லைத் தொடங்கவும் (இயல்புநிலை விநியோகத்தில்):

`wsl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஷெல்_கட்டளை</span>

- ஷெல்லைப் பயன்படுத்தாமல் லினக்ஸ் கட்டளையை இயக்கவும்:

`wsl --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை_வாதங்கள்</span>

- குறிப்பிட்ட விநியோகத்தைக் குறிப்பிடவும்:

`wsl --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விநியோகம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஷெல்_கட்டளை</span>

- கிடைக்கக்கூடிய விநியோகங்களின் பட்டியல்:

`wsl --list`

- விநியோகத்தை `.tar` கோப்பிற்கு ஏற்றுமதி செய்யவும்:

`wsl --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விநியோகம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை\டு\விநியோக_கோப்பு.tar</span>

- `.tar` கோப்பிலிருந்து விநியோகத்தை இறக்குமதி செய்:

`wsl --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விநியோகம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை\டு\நிறுவல்_இடம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/விநியோக_கோப்பு.tar</span>

- குறிப்பிட்ட விநியோகத்திற்கு பயன்படுத்தப்படும் `wsl` பதிப்பை மாற்றவும்:

`wsl --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விநியோகம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பதிப்பு</span>

- லினக்ஸிற்கான விண்டோஸ் துணை அமைப்பை மூடவும்:

`wsl --shutdown`
