---
layout: page
title: windows/curl (தமிழ்)
description: "PowerShell இல், அசல் `curl` நிரல் (<https://curl.se>) சரியாக நிறுவப்படாதபோது இந்தக் கட்டளை `Invoke-WebRequest` என்பதன் மாற்றுப்பெயராக இருக்கலாம்."
content_hash: 44d7a0b4e28038e74cbac0997bff7c3c506b120c
last_modified_at: 2022-12-03
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

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/curl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># curl

PowerShell இல், அசல் `curl` நிரல் (<https://curl.se>) சரியாக நிறுவப்படாதபோது இந்தக் கட்டளை `Invoke-WebRequest` என்பதன் மாற்றுப்பெயராக இருக்கலாம்.

- அதன் பதிப்பு எண்ணை அச்சிட்டு `curl` சரியாக நிறுவப்பட்டுள்ளதா என்பதைச் சரிபார்க்கவும். இந்த கட்டளை பிழையாக மதிப்பிடப்பட்டால், PowerShell இந்த கட்டளையை `Invoke-WebRequest` உடன் மாற்றியிருக்கலாம்:

`curl --version`

- அசல் `curl` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr curl -p common`

- `tldr` கட்டளை வரி கிளையண்டின் பழைய பதிப்புகளில் அசல் `curl` கட்டளைக்கான ஆவணங்களைப் பார்க்கவும்:

`tldr curl -o common`

- PowerShell இன் `Invoke-WebRequest` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr invoke-webrequest`
