LiteBrowser — Python/Kivy Android link handler
================================================

What it does
------------
LiteBrowser is a link sink, not a full web browser. When Android sends it an
http:// or https:// link, it briefly starts and exits without loading the page
or forwarding the link to Chrome. Opening LiteBrowser from its app icon shows
setup instructions.

This only works for links that Android hands to LiteBrowser. Set it as your
default browser/link handler, or choose it in Android's app chooser when
prompted. Some apps explicitly launch Chrome or another app; LiteBrowser cannot
intercept those launches. It also does not block ads inside apps or on websites.
Android may show a chooser before LiteBrowser has been selected as the default.

LiteBrowser does not request the INTERNET permission. The APK built with Kivy
includes the Python/Kivy runtime, so it is larger than a small native Android
application.

Build on a computer (Linux is recommended)
------------------------------------------
1. Install Python 3, Java JDK, and the Android build dependencies required by
   Buildozer. See the official guide:
   https://buildozer.readthedocs.io/
2. In this project folder, create and activate a Python virtual environment.
3. Install Buildozer:
       pip install --upgrade buildozer
4. Build a debug APK:
       buildozer android debug
5. Find the APK in the bin/ folder, transfer it to your phone, and install it.

Build without a computer (GitHub Actions)
------------------------------------------
The workflow at .github/workflows/build-apk.yml builds an APK on pushes to main
and can also be started manually:

1. Open this repository's Actions tab.
2. Select "Build LiteBrowser APK" and choose "Run workflow".
3. When the run succeeds, download the "LiteBrowser-APK" artifact and extract
the APK from it.
4. Install the APK on your Android phone.

Set as default browser/link handler
-----------------------------------
Open Android Settings > Apps > Default apps > Browser app and select LiteBrowser.
Menu names vary by Android version and manufacturer. If LiteBrowser is not
listed, open an http/https link and check whether Android offers it in the app
chooser. To undo the setting, choose Chrome or another browser in the same
Default apps screen.

Troubleshooting
---------------
- Buildozer builds are best done on Linux, not directly on an Android phone.
- The first build downloads Android SDK/NDK components and can take a while.
- If LiteBrowser is not offered for links, check the generated APK manifest
  for the HTTP and HTTPS VIEW intent filters in browser_intent_filters.xml.
- This app cannot override apps that explicitly open Chrome and cannot serve as
  a system-wide advertisement blocker.
