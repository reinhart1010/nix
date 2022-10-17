---
layout: page
title: linux/pacman-upgrade (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: 356a73a4adc55803c84fd0aaebb4245354427696
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman --upgrade

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- கோப்புகளிலிருந்து ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை நிறுவவும்:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு2.pkg.tar.zst</span>

- கேட்காமல் ஒரு தொகுப்பை நிறுவவும்:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு.pkg.tar.zst</span>

- தொகுப்பு நிறுவலின் போது முரண்பட்ட கோப்புகளை மேலெழுதவும்:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு.pkg.tar.zst</span>

- சார்பு பதிப்பு சரிபார்ப்புகளைத் தவிர்த்து, தொகுப்பை நிறுவவும்:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு.pkg.tar.zst</span>

- பாதிக்கப்படக்கூடிய தொகுப்புகளைப் பட்டியலிடுங்கள் (எந்த தொகுப்புகளையும் நிறுவாது):

`pacman --query --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு.pkg.tar.zst</span>

- உதவியைக் காட்டு:

`pacman --upgrade --help`
