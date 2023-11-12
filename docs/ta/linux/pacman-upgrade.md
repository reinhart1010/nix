---
layout: page
title: linux/pacman-upgrade (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: 3e74eb9aef766ff11c3ddf07faf3ae3772214173
last_modified_at: 2023-11-12
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
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
இதையும் பார்க்கவும்: `pacman`.
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

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு.pkg.tar.zst</span>

- உதவியைக் காட்டு:

`pacman --upgrade --help`
