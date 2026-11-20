LiteBrowser — Python/Kivy Android browser-link handler
======================================================

What it does
------------
- Registers as a handler for ordinary http:// and https:// links.
- When selected, opens briefly and exits cleanly.
- Does not display pages, redirect links, or request INTERNET permission.

Important
---------
This is NOT a real web browser. It is a link sink intended to stop unwanted
browser launches. Android may still show a chooser, and some apps may ignore
the selected handler or open Chrome directly. It cannot guarantee that every
advertisement is blocked.

The APK built with Kivy is not as small as a native Android app because it
bundles the Python/Kivy runtime. A tiny native Android implementation would
be substantially smaller, but would not be a Python-only app.

Build on a computer (Linux is recommended)
------------------------------------------
1. Install Python 3, Java JDK, and the Android build dependencies required by
   Buildozer. See the official guide:
   https://buildozer.readthedocs.io/
2. In this project folder, create/activate a Python virtual environment.
3. Install Buildozer:
       pip install --upgrade buildozer
4. Build the debug APK:
       buildozer android debug
5. The APK should appear in the bin/ folder.

Then transfer the APK to your Android phone and install it.

Set as browser/link handler
---------------------------
On Android, open Settings > Apps > Default apps > Browser app.
If LiteBrowser appears, select it. Menu wording varies by Android version
and manufacturer. If it does not appear, open an http/https link and check
whether Android offers LiteBrowser in the app chooser.

To undo it, choose Chrome or another browser in the same Default apps screen.

Troubleshooting
---------------
- Buildozer builds are best done on Linux, not directly on an Android phone.
- The first build downloads Android SDK/NDK components and can take a while.
- If the app does not appear as a browser, check the generated APK manifest
  to confirm both VIEW intent filters were merged into PythonActivity.
Build without owning a PC (GitHub Actions)
------------------------------------------
This project includes .github/workflows/build-apk.yml.

1. Sign in to https://github.com on your phone (create a free account if needed).
2. Create a NEW repository. Public is simplest for a first project; private is also
   possible subject to GitHub's Actions usage limits.
3. Upload the CONTENTS of this ZIP to the repository's main branch. Make sure the
   .github/workflows/build-apk.yml file is included. Android file managers sometimes
   hide folders beginning with a dot; enable hidden files if necessary.
4. Open the repository's Actions tab. If prompted, enable Actions.
5. Open "Build LiteBrowser APK", tap "Run workflow", then "Run workflow" again.
   A push to main also starts a build automatically.
6. Wait for the run to finish with a green check. Open that run and scroll to
   Artifacts. Download "LiteBrowser-APK".
7. Extract the downloaded artifact ZIP; it contains the APK. Install it on Android.

The first build can take several minutes and may fail if upstream Android build
dependencies change. If it fails, open the run and inspect the build log.

GitHub Actions provides a temporary build runner, not a permanent remote desktop.
