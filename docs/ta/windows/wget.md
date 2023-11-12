---
layout: page
title: windows/wget (தமிழ்)
description: "PowerShell இல், அசல் `wget` நிரல் (<https://www.gnu.org/software/wget>) சரியாக நிறுவப்படாதபோது இந்தக் கட்டளை `Invoke-WebRequest` என்பதன் மாற்றுப் பெயராக இருக்கலாம்."
content_hash: 3d0c9b28339944514e9473481a3f140ad09b89ec
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/windows/wget.html
    icon: bi bi-globe
  - title: bosanski version
    url: /bs/windows/wget.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/wget.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/windows/wget.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/wget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wget.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/wget.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/wget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/wget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/wget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/wget.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/wget.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/wget.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/windows/wget.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/windows/wget.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/windows/wget.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/wget.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/windows/wget.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/wget.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/windows/wget.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/wget.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/windows/wget.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/wget.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/windows/wget.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/windows/wget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/wget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/wget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wget

PowerShell இல், அசல் `wget` நிரல் (<https://www.gnu.org/software/wget>) சரியாக நிறுவப்படாதபோது இந்தக் கட்டளை `Invoke-WebRequest` என்பதன் மாற்றுப் பெயராக இருக்கலாம்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- அதன் பதிப்பு எண்ணை அச்சிட்டு `wget` சரியாக நிறுவப்பட்டுள்ளதா என்பதைச் சரிபார்க்கவும். இந்த கட்டளை பிழையாக மதிப்பிடப்பட்டால், PowerShell இந்த கட்டளையை `Invoke-WebRequest` உடன் மாற்றியிருக்கலாம்:

`curl --version`

- அசல் `wget` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr wget -p common`

- `tldr` கட்டளை வரி கிளையண்டின் பழைய பதிப்புகளில் அசல் `wget` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr wget -o common`

- PowerShell இன் 'Invoke-WebRequest' கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr invoke-webrequest`
