---
layout: page
title: windows/del (தமிழ்)
description: "ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளை நீக்கவும்."
content_hash: da8ae76e02a466a57af9d3d0176059743a463231
related_topics:
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># del

ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளை நீக்கவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட இடத்தால் பிரிக்கப்பட்ட கோப்புகள் அல்லது வடிவங்களை நீக்கவும்:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_வடிவம்</span>

- ஒவ்வொரு கோப்பையும் நீக்குவதற்கு முன் உறுதிப்படுத்தும்படி கேட்கவும்:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_வடிவம்</span>` /p`

- படிக்க மட்டுமேயான கோப்புகளை நீக்க கட்டாயப்படுத்துங்கள்:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_வடிவம்</span>` /f`

- எல்லா துணை அடைவுகளிலிருந்தும் கோப்பு(களை) மீண்டும் மீண்டும் நீக்கவும்:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_வடிவம்</span>` /s`

- உலகளாவிய வைல்டு கார்டின் அடிப்படையில் கோப்புகளை நீக்கும் போது கேட்க வேண்டாம்:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_வடிவம்</span>` /q`

- உதவி மற்றும் கிடைக்கக்கூடிய பண்புகளை பட்டியலிடு:

`del /?`

- குறிப்பிட்ட பண்புக்கூறுகளின் அடிப்படையில் கோப்புகளை நீக்கவும்:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_வடிவம்</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பண்புக்கூறு</span>