---
layout: page
title: windows/winget (தமிழ்)
description: "விண்டோஸ் தொகுப்பு மேலாளர் CLI."
content_hash: babe07d526c42ab18fcfd4c8e64c60ab57840813
last_modified_at: 2023-06-08
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># winget

விண்டோஸ் தொகுப்பு மேலாளர் CLI.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows/package-manager/winget>.

- ஒரு தொகுப்பை நிறுவவும்:

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- தொகுப்பை அகற்று (குறிப்பு: `uninstall` என்பதற்குப் பதிலாக `remove` என்பதும் பயன்படுத்தப்படலாம்):

`winget uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- ஒரு தொகுப்பு பற்றிய தகவலை காட்டு:

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- ஒரு தொகுப்பை தேடுங்கள்:

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- அனைத்து தொகுப்புகளையும் சமீபத்திய பதிப்புகளுக்கு மேம்படுத்தவும்:

`winget upgrade --all`

- `winget` மூலம் நிர்வகிக்கக்கூடிய நிறுவப்பட்ட அனைத்து தொகுப்புகளையும் பட்டியலிடுங்கள்:

`winget list --source winget`

- ஒரு கோப்பிலிருந்து தொகுப்புகளை இறக்குமதி செய்யவும் அல்லது நிறுவப்பட்ட தொகுப்புகளை ஒரு கோப்பிற்கு ஏற்றுமதி செய்யவும்:

`winget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import|export</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--import-file|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- winget-pkgs களஞ்சியத்தில் PR ஐச் சமர்ப்பிக்கும் முன் மேனிஃபெஸ்ட்டைச் சரிபார்க்கவும்:

`winget validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மேனிஃபெஸ்ட்</span>
