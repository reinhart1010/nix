---
layout: page
title: windows/add-appxpackage (हिन्दी)
description: "उपयोगकर्ता खाते में एक हस्ताक्षरित ऐप पैकेज (`.appx`, `.msix`, `.appxbundle` और `.msixbundle`) जोड़ने के लिए एक PowerShell उपयोगिता।"
content_hash: 643bf2f67aee6eaf3ca43c1b3c4215dba1ee4952
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/windows/add-appxpackage.html
    icon: bi bi-globe
---
# add-appxpackage

उपयोगकर्ता खाते में एक हस्ताक्षरित ऐप पैकेज (`.appx`, `.msix`, `.appxbundle` और `.msixbundle`) जोड़ने के लिए एक PowerShell उपयोगिता।
अधिक जानकारी: <https://learn.microsoft.com/powershell/module/appx/add-appxpackage>.

- एक ऐप पैकेज जोड़ें:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज.msix\का\पथ</span>

- निर्भरता के साथ एक ऐप पैकेज जोड़ें:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज.msix\का\पथ</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्भरता.msix\का\पथ</span>

- ऐप इंस्टॉलर फ़ाइल का उपयोग करके एक ऐप इंस्टॉल करें:

`add-appxpackage -AppInstallerFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप_इंस्टॉलर.msix\का\पथ</span>

- एक अहस्ताक्षरित पैकेज जोड़ें:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज.msix\का\पथ</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्भरता.msix\का\पथ</span>` -AllowUnsigned`
