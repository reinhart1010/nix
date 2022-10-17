---
layout: page
title: windows/curl (தமிழ்)
description: "PowerShell இல், அசல் `curl` நிரல் (<https://curl.se>) சரியாக நிறுவப்படாதபோது இந்தக் கட்டளை `Invoke-WebRequest` என்பதன் மாற்றுப்பெயராக இருக்கலாம்."
content_hash: 302d6c474ddb2e40d24ac557f211ac3c0f4743c0
related_topics:
  - title: Deutsch version
    url: /de/windows/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/curl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/curl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># curl

PowerShell இல், அசல் `curl` நிரல் (<https://curl.se>) சரியாக நிறுவப்படாதபோது இந்தக் கட்டளை `Invoke-WebRequest` என்பதன் மாற்றுப்பெயராக இருக்கலாம்.

- அதன் பதிப்பு எண்ணை அச்சிட்டு `curl` சரியாக நிறுவப்பட்டுள்ளதா என்பதைச் சரிபார்க்கவும். இந்த கட்டளை பிழையாக மதிப்பிடப்பட்டால், PowerShell இந்த கட்டளையை `Invoke-WebRequest` உடன் மாற்றியிருக்கலாம்:

`curl --version`

- அசல் `curl` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr curl -p common`

- PowerShell இன் `Invoke-WebRequest` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr invoke-webrequest`
