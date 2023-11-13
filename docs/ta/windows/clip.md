---
layout: page
title: windows/clip (தமிழ்)
description: "உள்ளீட்டு உள்ளடக்கத்தை விண்டோஸ் கிளிப்போர்டுக்கு நகலெடுக்கவும்."
content_hash: 739f73eddff1e8707f543a59bf91704cd1e8ec06
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/windows/clip.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/clip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/clip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clip

உள்ளீட்டு உள்ளடக்கத்தை விண்டோஸ் கிளிப்போர்டுக்கு நகலெடுக்கவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- விண்டோஸ் கிளிப்போர்டுக்கு குழாய் கட்டளை வரி வெளியீடு:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- ஒரு கோப்பின் உள்ளடக்கங்களை விண்டோஸ் கிளிப்போர்டுக்கு நகலெடுக்கவும்:

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.ext\பாதை</span>

- விண்டோஸ் கிளிப்போர்டுக்கு புதிய வரியுடன் உரையை நகலெடுக்கவும்:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஏதாவது உரை</span>` | clip`

- விண்டோஸ் கிளிப்போர்டுக்கு புதிய வரி இல்லாமல் உரையை நகலெடுக்கவும்:

`echo | set /p="ஏதாவது உரை" | clip`
