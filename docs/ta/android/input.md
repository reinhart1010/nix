---
layout: page
title: android/input (தமிழ்)
description: "நிகழ்வுக் குறியீடுகள் அல்லது தொடுதிரை சைகைகளை ஆண்ட்ராய்டு சாதனத்திற்கு அனுப்பவும்."
content_hash: a83333ab4c35225c58d627a0f90c7ac693644b63
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/android/input.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/input.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/input.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/input.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/input.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/input.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/input.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/input.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/input.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/input.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/input.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/input.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/input.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/input.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/input.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/input.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/input.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/input.html
    icon: bi bi-globe
tldri18n_status: 2
---
# input

நிகழ்வுக் குறியீடுகள் அல்லது தொடுதிரை சைகைகளை ஆண்ட்ராய்டு சாதனத்திற்கு அனுப்பவும்.
இந்தக் கட்டளையை `adb shell` மூலம் மட்டுமே பயன்படுத்த முடியும்.
மேலும் விவரத்திற்கு: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- ஆண்ட்ராய்டு சாதனத்திற்கு ஒற்றை எழுத்துக்கான நிகழ்வுக் குறியீட்டை அனுப்பவும்:

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிகழ்வு_குறியீடு</span>

- ஆண்ட்ராய்டு சாதனத்திற்கு உரையை அனுப்பு (`%s` என்பது இடைவெளிகளைக் குறிக்கிறது):

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">உரை</span>`"`

- ஆண்ட்ராய்டு சாதனத்திற்கு ஒரு முறை தட்டவும்:

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எக்ஸ்_போஸ்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஒய்_போஸ்</span>

- ஆண்ட்ராய்டு சாதனத்திற்கு ஸ்வைப் சைகையை அனுப்பவும்:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எக்ஸ்_தொடக்கம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஒய்_தொடக்கம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எக்ஸ்_முடிவு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஒய்_முடிவு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">காலம்_மில்லி_வினாடியில்</span>

- ஸ்வைப் சைகையைப் பயன்படுத்தி ஆண்ட்ராய்டு சாதனத்திற்கு நீண்ட அழுத்தத்தை அனுப்பவும்:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எக்ஸ்_போஸ்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஒய்_போஸ்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">எக்ஸ்_போஸ்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஒய்_போஸ்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">காலம்_மில்லி_வினாடியில்</span>
