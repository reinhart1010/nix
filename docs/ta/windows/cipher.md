---
layout: page
title: windows/cipher (தமிழ்)
description: "NTFS டிரைவ்களில் உள்ள கோப்புகளை குறியாக்கம் அல்லது மறைகுறியாக்கம் செய்யவும்."
content_hash: ac74f2f5c19b3701605ee8331631a1f4c088281b
last_modified_at: 2022-12-03
related_topics:
  - title: English version
    url: /en/windows/cipher.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cipher.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/cipher.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cipher

NTFS டிரைவ்களில் உள்ள கோப்புகளை குறியாக்கம் அல்லது மறைகுறியாக்கம் செய்யவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- ஒரு குறிப்பிட்ட மறைகுறியாக்கப்பட்ட கோப்பு அல்லது கோப்பகம் பற்றிய தகவலைக் காண்பி:

`cipher /c:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு_அல்லது_அடைவு</span>

- ஒரு கோப்பு அல்லது கோப்பகத்தை குறியாக்கு (கோப்பகத்தில் பின்னர் சேர்க்கப்பட்ட கோப்புகளும் கோப்பகம் குறிக்கப்பட்டதால் குறியாக்கம் செய்யப்படுகின்றன):

`cipher /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு_அல்லது_அடைவு</span>

- ஒரு கோப்பு அல்லது கோப்பகத்தை மறைகுறியாக்கவும்:

`cipher /d:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு_அல்லது_அடைவு</span>

- ஒரு கோப்பு அல்லது கோப்பகத்தை பாதுகாப்பாக அகற்றவும்:

`cipher /w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு_அல்லது_அடைவு</span>
