---
layout: page
title: windows/choice (தமிழ்)
description: "ஒரு தேர்வைத் தேர்ந்தெடுத்து, தேர்ந்தெடுக்கப்பட்ட தேர்வுக் குறியீட்டை வழங்க பயனரைத் தூண்டவும்."
content_hash: eea8aff10fc0d6a0adc833116ca912161c9410a6
last_modified_at: 2023-10-27
related_topics:
  - title: English version
    url: /en/windows/choice.html
    icon: bi bi-globe
---
# choice

ஒரு தேர்வைத் தேர்ந்தெடுத்து, தேர்ந்தெடுக்கப்பட்ட தேர்வுக் குறியீட்டை வழங்க பயனரைத் தூண்டவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/choice>.

- தற்போதைய பயனரை `Y` அல்லது `N` தேர்வைத் தேர்ந்தெடுக்கும்படி கேட்கவும்:

`choice`

- ஒரு குறிப்பிட்ட தொகுப்பிலிருந்து ஒரு [c]hoice ஐ தேர்ந்தெடுக்க தற்போதைய பயனரை கேட்கவும்:

`choice /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AB</span>

- குறிப்பிட்ட [m]செய்தியுடன் ஒரு தேர்வைத் தேர்ந்தெடுக்க தற்போதைய பயனரைத் தூண்டவும்:

`choice /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செய்தி</span>`"`

- ஒரு குறிப்பிட்ட தொகுப்பிலிருந்து ஒரு [c]கேஸ்-[s]சென்சிட்டிவ் [c]தேர்வு ஐத் தேர்ந்தெடுக்க தற்போதைய பயனரைத் தூண்டவும்:

`choice /cs /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ab</span>

- ஒரு தேர்வைத் தேர்ந்தெடுக்க தற்போதைய பயனரைத் தூண்டவும் மற்றும் ஒரு குறிப்பிட்ட [t] நேரத்தில் [d]இயல்புநிலை தேர்வை விரும்பவும்:

`choice /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- உதவியை காட்டு:

`choice /?`
