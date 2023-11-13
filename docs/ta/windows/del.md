---
layout: page
title: windows/del (தமிழ்)
description: "ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளை நீக்கவும்."
content_hash: 8d77fc16765e735a62ccbc0af4f19bf30a26abb3
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># del

ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளை நீக்கவும்.
PowerShell இல், இந்த கட்டளை `Remove-Item` என்பதன் மாற்றுப் பெயராகும். இந்த ஆவணம் `del` இன் கட்டளை வரியில் (`cmd`) பதிப்பை அடிப்படையாகக் கொண்டது.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- சமமான PowerShell கட்டளையின் ஆவணங்களைக் காண்க:

`tldr remove-item`

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
