---
layout: page
title: windows/doskey (தமிழ்)
description: "மேக்ரோக்கள், விண்டோஸ் கட்டளைகள் மற்றும் கட்டளை வரிகளை நிர்வகிக்கவும்."
content_hash: 5ba15e80740d7e45d127c0587f4afbc2e7ad02b9
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/doskey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/doskey.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/doskey.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/doskey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doskey

மேக்ரோக்கள், விண்டோஸ் கட்டளைகள் மற்றும் கட்டளை வரிகளை நிர்வகிக்கவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- கிடைக்கக்கூடிய மேக்ரோக்களை பட்டியலிடுங்கள்:

`doskey /macros`

- புதிய மேக்ரோவை உருவாக்கவும்:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>`"`

- ஒரு குறிப்பிட்ட இயங்கக்கூடியவைக்கு ஒரு புதிய மேக்ரோவை உருவாக்கவும்:

`doskey /exename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இயங்கக்கூடியவை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>`"`

- ஒரு மேக்ரோவை அகற்று:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>` =`

- நினைவகத்தில் சேமிக்கப்பட்ட அனைத்து கட்டளைகளையும் காண்பி:

`doskey /history`

- பெயர்வுத்திறனுக்காக மேக்ரோக்களை ஒரு கோப்பில் சேமிக்கவும்:

`doskey /macros > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macinit</span>

- ஒரு கோப்பிலிருந்து மேக்ரோக்களை ஏற்றவும்:

`doskey /macrofile = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macinit</span>
