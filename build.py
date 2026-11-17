"""Erzeugt die statischen Seiten der vBADBULLv-Website (EN + DE).

Aufruf:  python build.py <github-benutzername>
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
USER = sys.argv[1] if len(sys.argv) > 1 else "USERNAME"
BASE = f"https://{USER.lower()}.github.io/vbadbullv/"
REPO = f"https://github.com/{USER}/vbadbullv"
MAIL = "vbadbullv@gmail.com"
UPDATED = {"en": "17 November 2026", "de": "17. November 2026"}

BRAND = '<span>v</span>BADBULL<span>v</span>'

# key -> (EN-Datei, DE-Datei)
FILES = {
    "home": ("index.html", "de/index.html"),
    "privacy": ("privacy.html", "de/datenschutz.html"),
    "terms": ("terms.html", "de/nutzungsbedingungen.html"),
    "deletion": ("data-deletion.html", "de/datenloeschung.html"),
    "contact": ("contact.html", "de/kontakt.html"),
}
NAV = {
    "en": [("home", "Home"), ("privacy", "Privacy Policy"), ("terms", "Terms of Service"),
           ("deletion", "Data Deletion"), ("contact", "Contact")],
    "de": [("home", "Start"), ("privacy", "Datenschutz"), ("terms", "Nutzungsbedingungen"),
           ("deletion", "Datenlöschung"), ("contact", "Kontakt")],
}
UI = {
    "en": {"skip": "Skip to content", "updated": "Last updated", "other": "DE", "other_label": "Deutsch",
           "disclaimer": "vBADBULLv is a personal, non-commercial project. It is not affiliated with, endorsed or "
                         "sponsored by YouTube, Google, TikTok, Meta, Instagram, Twitch or any game publisher. "
                         "All trademarks belong to their respective owners.",
           "source": "Source code of this website"},
    "de": {"skip": "Zum Inhalt springen", "updated": "Stand", "other": "EN", "other_label": "English",
           "disclaimer": "vBADBULLv ist ein privates, nicht-kommerzielles Projekt. Es steht in keiner Verbindung zu "
                         "YouTube, Google, TikTok, Meta, Instagram, Twitch oder einem Spielepublisher und wird von "
                         "diesen weder unterstützt noch gesponsert. Alle Marken gehören ihren jeweiligen Inhabern.",
           "source": "Quellcode dieser Website"},
}

L = {  # externe Links
    "yt_tos": "https://www.youtube.com/t/terms",
    "g_privacy": "https://policies.google.com/privacy",
    "g_privacy_legacy": "http://www.google.com/policies/privacy",
    "g_revoke": "https://security.google.com/settings/security/permissions",
    "g_udp": "https://developers.google.com/terms/api-services-user-data-policy",
    "tt_tos": "https://www.tiktok.com/legal/terms-of-service",
    "tt_privacy": "https://www.tiktok.com/legal/privacy-policy",
    "ig_terms": "https://help.instagram.com/581066165581870",
    "meta_privacy": "https://www.facebook.com/privacy/policy/",
    "meta_platform": "https://developers.facebook.com/terms/",
    "tw_tos": "https://www.twitch.tv/p/legal/terms-of-service/",
    "tw_privacy": "https://www.twitch.tv/p/legal/privacy-notice/",
    "gh_privacy": "https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement",
}


def a(href, text):
    return f'<a href="{href}" rel="noopener">{text}</a>'


def mailto(subject=""):
    q = f"?subject={subject.replace(' ', '%20')}" if subject else ""
    return f'<a href="mailto:{MAIL}{q}">{MAIL}</a>'


# --------------------------------------------------------------------------- Inhalte

def home(lang, link):
    if lang == "en":
        return f"""
<section class="hero">
  <h1>{BRAND}</h1>
  <p class="tag">Clip uploader for my own gameplay channels</p>
  <p class="lead">vBADBULLv is a small personal desktop tool. It takes gameplay clips I recorded myself and uploads
  them – with title, description, tags and visibility – to <strong>my own</strong> channels and accounts, using each
  platform's official API and official sign-in.</p>
  <div class="buttons">
    <a class="btn btn-pink" href="{link('privacy')}">Privacy Policy</a>
    <a class="btn btn-ghost" href="{link('terms')}">Terms of Service</a>
    <a class="btn btn-ghost" href="{link('deletion')}">Data Deletion</a>
  </div>
</section>

<section class="card" id="about">
  <h2>What is vBADBULLv?</h2>
  <p>vBADBULLv is the name of my creator channels and of the small app I built to publish to them. The app runs
  locally on my own computer. It is <strong>not</strong> a public service: there is no sign-up, no user accounts,
  no server and no database. It is used only by me, the operator, to upload my own content to my own accounts.</p>
  <ul class="check">
    <li>Uploads video files I choose, with the title, description, tags and visibility I set (default: <em>private</em>).</li>
    <li>Signs in only through the platform's own official login page (OAuth) – the app never sees passwords.</li>
    <li>Never reads comments, messages, followers, analytics or anyone else's data.</li>
    <li>No ads, no tracking, no selling or sharing of data.</li>
  </ul>
</section>

<section class="card" id="how">
  <h2>How it works</h2>
  <ol class="steps">
    <li><strong>Record</strong><br>I record a gameplay clip on my PC.</li>
    <li><strong>Describe</strong><br>I start the tool and enter title, description, tags and visibility.</li>
    <li><strong>Sign in once</strong><br>The platform's official login opens in the browser. The access token is stored only on my computer.</li>
    <li><strong>Upload</strong><br>The tool sends the video directly to the platform's official API – nothing goes anywhere else.</li>
  </ol>
</section>

<section class="card" id="platforms">
  <h2>Platforms &amp; permissions</h2>
  <div class="grid3">
    <div class="tile"><h3>YouTube <span class="badge live">active</span></h3>
      <p>YouTube Data API v3. Permissions: <code>youtube.upload</code> to upload videos and <code>youtube.readonly</code>
      only to confirm that the correct channel is signed in. This app uses YouTube API Services.</p></div>
    <div class="tile"><h3>TikTok <span class="badge plan">planned</span></h3>
      <p>TikTok Content Posting API – uploading my own clips to my own TikTok account (<code>video.upload</code> / <code>video.publish</code>).</p></div>
    <div class="tile"><h3>Instagram <span class="badge plan">planned</span></h3>
      <p>Instagram API content publishing – posting my own clips as Reels to my own professional account.</p></div>
    <div class="tile"><h3>Twitch <span class="badge plan">planned</span></h3>
      <p>Twitch API – limited to managing clips and videos on my own channel. Twitch does not offer video uploads via API.</p></div>
  </div>
</section>

<section class="card" id="data">
  <h2>Your data at a glance</h2>
  <p>The only data the app keeps is the sign-in token for each connected account, stored locally on my computer.
  Videos and their texts are sent directly to the platform I upload to. Details are in the
  <a href="{link('privacy')}">Privacy Policy</a>; how to remove access and data is explained on the
  <a href="{link('deletion')}">Data Deletion</a> page. Questions? <a href="{link('contact')}">Contact</a> me.</p>
</section>
"""
    return f"""
<section class="hero">
  <h1>{BRAND}</h1>
  <p class="tag">Clip-Uploader für meine eigenen Gameplay-Kanäle</p>
  <p class="lead">vBADBULLv ist ein kleines, privates Desktop-Tool. Es lädt Gameplay-Clips, die ich selbst aufgenommen
  habe, mit Titel, Beschreibung, Tags und Sichtbarkeit auf <strong>meine eigenen</strong> Kanäle und Konten hoch –
  über die offizielle API und die offizielle Anmeldung der jeweiligen Plattform.</p>
  <div class="buttons">
    <a class="btn btn-pink" href="{link('privacy')}">Datenschutzerklärung</a>
    <a class="btn btn-ghost" href="{link('terms')}">Nutzungsbedingungen</a>
    <a class="btn btn-ghost" href="{link('deletion')}">Datenlöschung</a>
  </div>
</section>

<section class="card" id="about">
  <h2>Was ist vBADBULLv?</h2>
  <p>vBADBULLv ist der Name meiner Creator-Kanäle und der kleinen App, mit der ich dort veröffentliche. Die App läuft
  lokal auf meinem eigenen Computer. Sie ist <strong>kein</strong> öffentlicher Dienst: keine Registrierung, keine
  Benutzerkonten, kein Server, keine Datenbank. Nur ich als Betreiber nutze sie, um meine eigenen Inhalte auf meine
  eigenen Konten hochzuladen.</p>
  <ul class="check">
    <li>Lädt von mir ausgewählte Videodateien mit dem Titel, der Beschreibung, den Tags und der Sichtbarkeit hoch, die ich festlege (Standard: <em>privat</em>).</li>
    <li>Anmeldung ausschließlich über die offizielle Login-Seite der Plattform (OAuth) – die App sieht nie ein Passwort.</li>
    <li>Liest keine Kommentare, Nachrichten, Follower, Statistiken oder Daten anderer Personen.</li>
    <li>Keine Werbung, kein Tracking, kein Verkauf und keine Weitergabe von Daten.</li>
  </ul>
</section>

<section class="card" id="how">
  <h2>So funktioniert es</h2>
  <ol class="steps">
    <li><strong>Aufnehmen</strong><br>Ich nehme einen Gameplay-Clip auf meinem PC auf.</li>
    <li><strong>Beschreiben</strong><br>Ich starte das Tool und gebe Titel, Beschreibung, Tags und Sichtbarkeit ein.</li>
    <li><strong>Einmal anmelden</strong><br>Die offizielle Anmeldung der Plattform öffnet sich im Browser. Der Zugriffstoken wird nur auf meinem Computer gespeichert.</li>
    <li><strong>Hochladen</strong><br>Das Tool sendet das Video direkt an die offizielle API der Plattform – sonst nirgendwohin.</li>
  </ol>
</section>

<section class="card" id="platforms">
  <h2>Plattformen &amp; Berechtigungen</h2>
  <div class="grid3">
    <div class="tile"><h3>YouTube <span class="badge live">aktiv</span></h3>
      <p>YouTube Data API v3. Berechtigungen: <code>youtube.upload</code> zum Hochladen und <code>youtube.readonly</code>
      nur, um zu prüfen, dass der richtige Kanal angemeldet ist. Diese App nutzt YouTube API Services.</p></div>
    <div class="tile"><h3>TikTok <span class="badge plan">geplant</span></h3>
      <p>TikTok Content Posting API – Hochladen meiner eigenen Clips auf mein eigenes TikTok-Konto (<code>video.upload</code> / <code>video.publish</code>).</p></div>
    <div class="tile"><h3>Instagram <span class="badge plan">geplant</span></h3>
      <p>Instagram-API (Content Publishing) – Veröffentlichen meiner eigenen Clips als Reels auf meinem eigenen professionellen Konto.</p></div>
    <div class="tile"><h3>Twitch <span class="badge plan">geplant</span></h3>
      <p>Twitch-API – beschränkt auf die Verwaltung von Clips und Videos auf meinem eigenen Kanal. Twitch bietet keinen Video-Upload per API.</p></div>
  </div>
</section>

<section class="card" id="data">
  <h2>Deine Daten auf einen Blick</h2>
  <p>Die App speichert nur den Anmelde-Token je verbundenem Konto, und zwar lokal auf meinem Computer. Videos und
  ihre Texte gehen direkt an die Plattform, auf die ich hochlade. Einzelheiten stehen in der
  <a href="{link('privacy')}">Datenschutzerklärung</a>; wie Zugriff und Daten entfernt werden, steht unter
  <a href="{link('deletion')}">Datenlöschung</a>. Fragen? <a href="{link('contact')}">Kontakt</a>.</p>
</section>
"""


def privacy(lang, link):
    if lang == "en":
        return f"""
<h1>Privacy Policy</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>1. Who is responsible</h2>
<p>Controller for this website and the vBADBULLv app is the operator of the vBADBULLv channels
(“vBADBULLv”, “I”, “me”). Contact: {mailto('Privacy')}.</p>

<h2>2. What this policy covers</h2>
<p>This policy covers (a) this website and (b) the vBADBULLv app – a personal desktop tool that uploads my own
gameplay clips to my own accounts on YouTube and, once connected, TikTok, Instagram and Twitch. The app is used only
by me; it has no public user accounts. Anyone who signs in to it (for example during a platform's app review) is
covered by this policy in the same way.</p>

<h2>3. This website</h2>
<p>This website is hosted by GitHub Pages (GitHub, Inc., USA). When you open a page, GitHub processes technical data
such as your IP address, browser type and time of access in server logs to deliver the site and keep it secure – see
the {a(L['gh_privacy'], 'GitHub Privacy Statement')}. This website itself sets <strong>no cookies</strong>, uses
<strong>no analytics or tracking</strong> and loads <strong>no external fonts, scripts or embeds</strong>.
Legal basis: legitimate interest in a secure, working website (Art. 6(1)(f) GDPR).</p>

<h2>4. Data the app accesses</h2>
<ul>
<li><strong>Access and refresh tokens</strong> that a platform issues after you sign in on its official OAuth page.</li>
<li><strong>Basic account information</strong> (channel or account ID and name), used only to confirm that the correct account is signed in.</li>
<li><strong>Video files and metadata</strong> (title, description, tags, visibility) that I choose for an upload.</li>
</ul>
<p>The app does <strong>not</strong> access passwords, contacts, messages, comments, followers or subscribers,
analytics, payment data or any data of other users.</p>

<h2>5. How the data is used and shared</h2>
<p>The data is used for one purpose only: uploading the selected video to the selected account and confirming the
right account is used. Videos and metadata are sent <strong>directly</strong> from my computer to the respective
platform (Google/YouTube, TikTok, Meta/Instagram or Twitch). No data is sold, rented, shared with other third
parties, used for advertising or used to train AI models. Legal basis: your consent given on the platform's sign-in
screen (Art. 6(1)(a) GDPR), which you can withdraw at any time.</p>

<h2>6. Storage and retention</h2>
<p>Tokens are stored only locally on my own computer (for example in a file named <code>token.json</code>). They are
never uploaded to this website, a code repository or any server. Account information and API responses are not
stored beyond the running upload. Tokens are kept until access is revoked or deletion is requested; they are then
deleted without delay – at the latest within 7 days of a deletion request and within 30 days after access has been
revoked.</p>

<h2>7. YouTube API Services</h2>
<p>The vBADBULLv app uses <strong>YouTube API Services</strong>. By using it you agree to be bound by the
{a(L['yt_tos'], 'YouTube Terms of Service')}. Google's handling of data is described in the
{a(L['g_privacy_legacy'], 'Google Privacy Policy')}. You can revoke the app's access to your Google/YouTube data at
any time via the {a(L['g_revoke'], 'Google security settings page')}.</p>
<p class="notice">vBADBULLv's use and transfer of information received from Google APIs will adhere to the
{a(L['g_udp'], 'Google API Services User Data Policy')}, including the Limited Use requirements.</p>

<h2>8. TikTok, Instagram/Meta and Twitch</h2>
<p>The same rules apply to these platforms: only tokens are stored locally, uploads go directly to the platform, no
data is shared. Their own policies apply to data they process:
{a(L['tt_privacy'], 'TikTok Privacy Policy')}, {a(L['meta_privacy'], 'Meta Privacy Policy')} (also for Instagram),
{a(L['tw_privacy'], 'Twitch Privacy Notice')}. The app follows the {a(L['meta_platform'], 'Meta Platform Terms')}
and the platforms' developer terms.</p>

<h2>9. Deleting your data</h2>
<p>Step-by-step instructions for revoking access and requesting deletion are on the
<a href="{link('deletion')}">Data Deletion</a> page. You can also simply e-mail {mailto('Data deletion request')}.</p>

<h2>10. Your rights</h2>
<p>Under the GDPR you have the right to access, rectification, erasure, restriction of processing, data portability
and objection, and to withdraw consent at any time with effect for the future. You may also lodge a complaint with a
data protection supervisory authority.</p>

<h2>11. Children</h2>
<p>The app and this website are not directed at children under 16.</p>

<h2>12. Changes</h2>
<p>If the app or the law changes, this policy will be updated; the date at the top shows the current version.</p>

<h2>13. Contact</h2>
<p>{mailto('Privacy')} – see also the <a href="{link('contact')}">Contact</a> page.</p>
</div>
"""
    return f"""
<h1>Datenschutzerklärung</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>1. Verantwortlicher</h2>
<p>Verantwortlich für diese Website und die App vBADBULLv ist der Betreiber der vBADBULLv-Kanäle („vBADBULLv“,
„ich“). Kontakt: {mailto('Datenschutz')}.</p>

<h2>2. Geltungsbereich</h2>
<p>Diese Erklärung gilt für (a) diese Website und (b) die App vBADBULLv – ein privates Desktop-Tool, das meine eigenen
Gameplay-Clips auf meine eigenen Konten bei YouTube und, sobald verbunden, TikTok, Instagram und Twitch hochlädt.
Die App wird nur von mir genutzt; es gibt keine öffentlichen Benutzerkonten. Wer sich dennoch anmeldet (z. B. bei
einer App-Prüfung durch eine Plattform), ist von dieser Erklärung gleichermaßen erfasst.</p>

<h2>3. Diese Website</h2>
<p>Diese Website wird über GitHub Pages (GitHub, Inc., USA) bereitgestellt. Beim Aufruf verarbeitet GitHub technische
Daten wie IP-Adresse, Browsertyp und Zugriffszeit in Server-Logs, um die Seite auszuliefern und abzusichern – siehe
{a(L['gh_privacy'], 'GitHub Privacy Statement')}. Die Website selbst setzt <strong>keine Cookies</strong>, nutzt
<strong>kein Tracking und keine Analyse</strong> und lädt <strong>keine externen Schriften, Skripte oder
Einbettungen</strong>. Rechtsgrundlage: berechtigtes Interesse an einer sicheren, funktionierenden Website
(Art. 6 Abs. 1 lit. f DSGVO).</p>

<h2>4. Daten, auf die die App zugreift</h2>
<ul>
<li><strong>Zugriffs- und Aktualisierungstokens</strong>, die eine Plattform nach der Anmeldung auf ihrer offiziellen OAuth-Seite ausstellt.</li>
<li><strong>Grundlegende Kontoinformationen</strong> (Kanal- bzw. Konto-ID und Name), ausschließlich um zu prüfen, dass das richtige Konto angemeldet ist.</li>
<li><strong>Videodateien und Metadaten</strong> (Titel, Beschreibung, Tags, Sichtbarkeit), die ich für einen Upload auswähle.</li>
</ul>
<p>Die App greift <strong>nicht</strong> auf Passwörter, Kontakte, Nachrichten, Kommentare, Follower oder
Abonnenten, Statistiken, Zahlungsdaten oder Daten anderer Nutzer zu.</p>

<h2>5. Verwendung und Weitergabe</h2>
<p>Die Daten dienen nur einem Zweck: das ausgewählte Video auf das ausgewählte Konto hochzuladen und sicherzustellen,
dass das richtige Konto verwendet wird. Videos und Metadaten werden <strong>direkt</strong> von meinem Computer an
die jeweilige Plattform (Google/YouTube, TikTok, Meta/Instagram oder Twitch) übertragen. Es werden keine Daten
verkauft, vermietet, an sonstige Dritte weitergegeben, für Werbung genutzt oder zum Training von KI-Modellen
verwendet. Rechtsgrundlage: deine Einwilligung im Anmeldedialog der Plattform (Art. 6 Abs. 1 lit. a DSGVO), die du
jederzeit widerrufen kannst.</p>

<h2>6. Speicherung und Speicherdauer</h2>
<p>Tokens werden ausschließlich lokal auf meinem eigenen Computer gespeichert (z. B. in einer Datei
<code>token.json</code>). Sie werden nie auf diese Website, in ein Code-Repository oder auf einen Server hochgeladen.
Kontoinformationen und API-Antworten werden nicht über den laufenden Upload hinaus gespeichert. Tokens bleiben
gespeichert, bis der Zugriff widerrufen oder die Löschung verlangt wird; dann werden sie unverzüglich gelöscht –
spätestens 7 Tage nach einer Löschanfrage und 30 Tage nach einem Widerruf des Zugriffs.</p>

<h2>7. YouTube API Services</h2>
<p>Die App vBADBULLv nutzt <strong>YouTube API Services</strong>. Mit der Nutzung erklärst du dich an die
{a(L['yt_tos'], 'Nutzungsbedingungen von YouTube')} gebunden. Wie Google mit Daten umgeht, beschreibt die
{a(L['g_privacy_legacy'], 'Datenschutzerklärung von Google')}. Den Zugriff der App auf deine Google-/YouTube-Daten
kannst du jederzeit über die {a(L['g_revoke'], 'Sicherheitseinstellungen deines Google-Kontos')} widerrufen.</p>
<p class="notice">Die Nutzung und Übertragung von Informationen, die vBADBULLv von Google-APIs erhält, entspricht der
{a(L['g_udp'], 'Google API Services User Data Policy')} einschließlich der Anforderungen zur eingeschränkten Nutzung
(Limited Use).</p>

<h2>8. TikTok, Instagram/Meta und Twitch</h2>
<p>Für diese Plattformen gelten dieselben Regeln: nur Tokens werden lokal gespeichert, Uploads gehen direkt an die
Plattform, keine Weitergabe. Für die Datenverarbeitung durch die Plattformen gelten deren eigene Richtlinien:
{a(L['tt_privacy'], 'TikTok-Datenschutzrichtlinie')}, {a(L['meta_privacy'], 'Meta-Datenschutzrichtlinie')} (auch für
Instagram), {a(L['tw_privacy'], 'Twitch-Datenschutzhinweis')}. Die App hält die
{a(L['meta_platform'], 'Meta-Plattform-Nutzungsbedingungen')} und die Entwicklerbedingungen der Plattformen ein.</p>

<h2>9. Löschung deiner Daten</h2>
<p>Eine Schritt-für-Schritt-Anleitung zum Widerruf des Zugriffs und zur Löschanfrage findest du unter
<a href="{link('deletion')}">Datenlöschung</a>. Du kannst auch einfach an {mailto('Loeschanfrage')} schreiben.</p>

<h2>10. Deine Rechte</h2>
<p>Nach der DSGVO hast du das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung,
Datenübertragbarkeit und Widerspruch sowie das Recht, eine Einwilligung jederzeit mit Wirkung für die Zukunft zu
widerrufen. Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren.</p>

<h2>11. Kinder</h2>
<p>Die App und diese Website richten sich nicht an Kinder unter 16 Jahren.</p>

<h2>12. Änderungen</h2>
<p>Ändern sich die App oder die Rechtslage, wird diese Erklärung angepasst; das Datum oben zeigt die aktuelle Fassung.</p>

<h2>13. Kontakt</h2>
<p>{mailto('Datenschutz')} – siehe auch <a href="{link('contact')}">Kontakt</a>.</p>
</div>
"""


def terms(lang, link):
    if lang == "en":
        return f"""
<h1>Terms of Service</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>1. About the app</h2>
<p>vBADBULLv is a personal, non-commercial desktop tool operated by the owner of the vBADBULLv channels. It uploads
the operator's own gameplay clips to the operator's own accounts. It is provided free of charge and is not offered
as a public service.</p>

<h2>2. Who may use it</h2>
<p>The app is intended for use by the operator only. Anyone else who signs in (for example a platform reviewer)
may use it only to evaluate its functionality, and agrees to these terms and the
<a href="{link('privacy')}">Privacy Policy</a>.</p>

<h2>3. Platform terms</h2>
<p>The app uses <strong>YouTube API Services</strong>. By using the app you agree to be bound by the
{a(L['yt_tos'], 'YouTube Terms of Service')}; see also the {a(L['g_privacy'], 'Google Privacy Policy')}.
Uploads to other platforms are subject to their terms as well: {a(L['tt_tos'], 'TikTok Terms of Service')},
{a(L['ig_terms'], 'Instagram Terms of Use')}, {a(L['meta_platform'], 'Meta Platform Terms')} and
{a(L['tw_tos'], 'Twitch Terms of Service')}.</p>

<h2>4. Content</h2>
<p>Only content that the uploader created and has the rights to may be uploaded. Uploads must follow each platform's
community guidelines and copyright rules, including any rules of game publishers about sharing gameplay footage.
The uploader is solely responsible for uploaded content.</p>

<h2>5. No warranty</h2>
<p>The app is provided “as is”, without warranty of any kind. It may change or stop working at any time, for example
when a platform changes its API.</p>

<h2>6. Liability</h2>
<p>To the extent permitted by law, the operator is not liable for damages arising from the use of the app.
Liability for intent and gross negligence and for injury to life, body or health remains unaffected.</p>

<h2>7. No affiliation</h2>
<p>vBADBULLv is not affiliated with, endorsed or sponsored by YouTube, Google, TikTok, Meta, Instagram, Twitch or any
game publisher. All trademarks belong to their respective owners.</p>

<h2>8. Changes and contact</h2>
<p>These terms may be updated; the date at the top shows the current version. Questions: {mailto('Terms')}.</p>
</div>
"""
    return f"""
<h1>Nutzungsbedingungen</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>1. Über die App</h2>
<p>vBADBULLv ist ein privates, nicht-kommerzielles Desktop-Tool des Betreibers der vBADBULLv-Kanäle. Es lädt die
eigenen Gameplay-Clips des Betreibers auf dessen eigene Konten hoch. Es ist kostenlos und wird nicht als öffentlicher
Dienst angeboten.</p>

<h2>2. Wer die App nutzen darf</h2>
<p>Die App ist nur für die Nutzung durch den Betreiber bestimmt. Andere Personen, die sich anmelden (z. B. Prüfer
einer Plattform), dürfen sie nur zur Beurteilung ihrer Funktion verwenden und stimmen diesen Bedingungen und der
<a href="{link('privacy')}">Datenschutzerklärung</a> zu.</p>

<h2>3. Bedingungen der Plattformen</h2>
<p>Die App nutzt <strong>YouTube API Services</strong>. Mit der Nutzung der App erklärst du dich an die
{a(L['yt_tos'], 'Nutzungsbedingungen von YouTube')} gebunden; siehe auch die
{a(L['g_privacy'], 'Datenschutzerklärung von Google')}. Uploads auf andere Plattformen unterliegen ebenfalls deren
Bedingungen: {a(L['tt_tos'], 'TikTok-Nutzungsbedingungen')}, {a(L['ig_terms'], 'Instagram-Nutzungsbedingungen')},
{a(L['meta_platform'], 'Meta-Plattform-Nutzungsbedingungen')} und {a(L['tw_tos'], 'Twitch-Nutzungsbedingungen')}.</p>

<h2>4. Inhalte</h2>
<p>Hochgeladen werden dürfen nur Inhalte, die der Uploader selbst erstellt hat und an denen er die Rechte hat. Uploads
müssen die Community-Richtlinien und Urheberrechtsregeln der jeweiligen Plattform einhalten, einschließlich der Regeln
von Spielepublishern zum Teilen von Gameplay-Aufnahmen. Für hochgeladene Inhalte ist allein der Uploader
verantwortlich.</p>

<h2>5. Keine Gewährleistung</h2>
<p>Die App wird „wie besehen“ ohne Gewähr bereitgestellt. Sie kann sich jederzeit ändern oder nicht mehr
funktionieren, z. B. wenn eine Plattform ihre API ändert.</p>

<h2>6. Haftung</h2>
<p>Soweit gesetzlich zulässig, haftet der Betreiber nicht für Schäden aus der Nutzung der App. Die Haftung für
Vorsatz und grobe Fahrlässigkeit sowie für Schäden aus der Verletzung von Leben, Körper oder Gesundheit bleibt
unberührt.</p>

<h2>7. Keine Verbindung zu den Plattformen</h2>
<p>vBADBULLv steht in keiner Verbindung zu YouTube, Google, TikTok, Meta, Instagram, Twitch oder einem Spielepublisher
und wird von diesen weder unterstützt noch gesponsert. Alle Marken gehören ihren jeweiligen Inhabern.</p>

<h2>8. Änderungen und Kontakt</h2>
<p>Diese Bedingungen können angepasst werden; das Datum oben zeigt die aktuelle Fassung. Fragen: {mailto('Nutzungsbedingungen')}.</p>
</div>
"""


def deletion(lang, link):
    if lang == "en":
        return f"""
<h1>Data Deletion</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>What is stored</h2>
<p>vBADBULLv has no server and no database. The only data it keeps is the sign-in token for each connected account,
stored locally on the operator's computer. Uploaded videos live on the platform you uploaded them to and can be
deleted there like any other post.</p>

<h2>Option 1 – Remove access yourself</h2>
<p>Revoking access makes the stored token useless immediately; the local copy is then deleted as well.</p>
<h3>Google / YouTube</h3>
<p>Open the {a(L['g_revoke'], 'Google security settings page')} (Third-party apps &amp; services), select
<strong>vBADBULLv</strong> and choose <em>Delete all connections</em> / <em>Remove access</em>.</p>
<h3>TikTok</h3>
<p>In the TikTok app: <em>Profile → Menu (☰) → Settings and privacy → Security &amp; permissions → Apps and
services</em> (or <em>Manage app permissions</em>), select <strong>vBADBULLv</strong> and tap <em>Remove access</em>.</p>
<h3>Instagram / Facebook (Meta)</h3>
<p>Instagram: <em>Settings → Website permissions → Apps and websites → Active</em>, select <strong>vBADBULLv</strong>
and tap <em>Remove</em>. Facebook: <em>Settings &amp; privacy → Settings → Apps and websites</em>, select
<strong>vBADBULLv</strong> and choose <em>Remove</em>.</p>
<h3>Twitch</h3>
<p><em>Settings → Connections → Other connections</em>, find <strong>vBADBULLv</strong> and click <em>Disconnect</em>.</p>

<h2>Option 2 – Ask for deletion</h2>
<p>Send an e-mail to {mailto('Data deletion request')} with the subject <strong>“Data deletion request”</strong> and
the platform and account name concerned. All data relating to that account is deleted within <strong>7 days</strong>
and you receive a confirmation by e-mail.</p>
</div>
"""
    return f"""
<h1>Datenlöschung</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>Was gespeichert wird</h2>
<p>vBADBULLv hat keinen Server und keine Datenbank. Gespeichert wird nur der Anmelde-Token je verbundenem Konto, lokal
auf dem Computer des Betreibers. Hochgeladene Videos liegen auf der jeweiligen Plattform und können dort wie jeder
andere Beitrag gelöscht werden.</p>

<h2>Möglichkeit 1 – Zugriff selbst entfernen</h2>
<p>Nach dem Widerruf ist der gespeicherte Token sofort wertlos; die lokale Kopie wird danach ebenfalls gelöscht.</p>
<h3>Google / YouTube</h3>
<p>Öffne die {a(L['g_revoke'], 'Sicherheitseinstellungen deines Google-Kontos')} (Drittanbieter-Apps und -Dienste),
wähle <strong>vBADBULLv</strong> und klicke auf <em>Alle Verbindungen löschen</em> bzw. <em>Zugriff entfernen</em>.</p>
<h3>TikTok</h3>
<p>In der TikTok-App: <em>Profil → Menü (☰) → Einstellungen und Datenschutz → Sicherheit und Berechtigungen → Apps und
Dienste</em> (bzw. <em>App-Berechtigungen verwalten</em>), <strong>vBADBULLv</strong> auswählen und <em>Zugriff
entfernen</em> tippen.</p>
<h3>Instagram / Facebook (Meta)</h3>
<p>Instagram: <em>Einstellungen → Website-Berechtigungen → Apps und Websites → Aktiv</em>, <strong>vBADBULLv</strong>
auswählen und <em>Entfernen</em> tippen. Facebook: <em>Einstellungen und Privatsphäre → Einstellungen → Apps und
Websites</em>, <strong>vBADBULLv</strong> auswählen und <em>Entfernen</em> wählen.</p>
<h3>Twitch</h3>
<p><em>Einstellungen → Verknüpfungen → Andere Verknüpfungen</em>, <strong>vBADBULLv</strong> suchen und
<em>Verbindung trennen</em> klicken.</p>

<h2>Möglichkeit 2 – Löschung anfordern</h2>
<p>Schreibe eine E-Mail an {mailto('Loeschanfrage')} mit dem Betreff <strong>„Löschanfrage“</strong> und nenne
Plattform und Kontoname. Alle Daten zu diesem Konto werden innerhalb von <strong>7 Tagen</strong> gelöscht; du
erhältst eine Bestätigung per E-Mail.</p>
</div>
"""


def contact(lang, link):
    if lang == "en":
        return f"""
<h1>Contact</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>Get in touch</h2>
<p>For questions about the vBADBULLv app, this website, privacy or data deletion, write to:</p>
<p class="mail">{mailto()}</p>
<p>I usually reply within a few days. Data deletion requests are completed within 7 days – see
<a href="{link('deletion')}">Data Deletion</a>.</p>
<h3>Operator</h3>
<p>vBADBULLv – private, non-commercial project of the operator of the vBADBULLv creator channels.</p>
</div>
"""
    return f"""
<h1>Kontakt</h1>
<p class="meta">{UI[lang]['updated']}: {UPDATED[lang]}</p>
<div class="card">
<h2>Schreib mir</h2>
<p>Bei Fragen zur App vBADBULLv, zu dieser Website, zum Datenschutz oder zur Datenlöschung:</p>
<p class="mail">{mailto()}</p>
<p>Ich antworte in der Regel innerhalb weniger Tage. Löschanfragen werden innerhalb von 7 Tagen erledigt – siehe
<a href="{link('deletion')}">Datenlöschung</a>.</p>
<h3>Betreiber</h3>
<p>vBADBULLv – privates, nicht-kommerzielles Projekt des Betreibers der vBADBULLv-Creator-Kanäle.</p>
</div>
"""


CONTENT = {"home": home, "privacy": privacy, "terms": terms, "deletion": deletion, "contact": contact}
META = {
    "home": {"en": ("vBADBULLv – Clip uploader for my own gameplay channels",
                    "vBADBULLv is a personal tool that uploads my own gameplay clips to my own YouTube, TikTok, Instagram and Twitch accounts."),
             "de": ("vBADBULLv – Clip-Uploader für meine eigenen Gameplay-Kanäle",
                    "vBADBULLv ist ein privates Tool, das meine eigenen Gameplay-Clips auf meine eigenen YouTube-, TikTok-, Instagram- und Twitch-Konten hochlädt.")},
    "privacy": {"en": ("Privacy Policy – vBADBULLv", "Privacy Policy of the vBADBULLv app and website."),
                "de": ("Datenschutzerklärung – vBADBULLv", "Datenschutzerklärung der App und Website vBADBULLv.")},
    "terms": {"en": ("Terms of Service – vBADBULLv", "Terms of Service of the vBADBULLv app."),
              "de": ("Nutzungsbedingungen – vBADBULLv", "Nutzungsbedingungen der App vBADBULLv.")},
    "deletion": {"en": ("Data Deletion – vBADBULLv", "How to remove vBADBULLv's access and delete your data."),
                 "de": ("Datenlöschung – vBADBULLv", "So entfernst du den Zugriff von vBADBULLv und lässt deine Daten löschen.")},
    "contact": {"en": ("Contact – vBADBULLv", "Contact the operator of vBADBULLv."),
                "de": ("Kontakt – vBADBULLv", "Kontakt zum Betreiber von vBADBULLv.")},
}

SCENE = """<div class="scene" aria-hidden="true">
  <div class="stars"></div><div class="sun"></div><div class="floor"></div><div class="horizon"></div>
  <img class="palm l1" src="{p}assets/palm.svg" alt=""><img class="palm l2" src="{p}assets/palm.svg" alt="">
  <img class="palm r1" src="{p}assets/palm.svg" alt=""><img class="palm r2" src="{p}assets/palm.svg" alt="">
</div>"""


def url(f):
    return BASE + (f[:-len("index.html")] if f.endswith("index.html") else f)


def render(key, lang):
    idx = 0 if lang == "en" else 1
    this = FILES[key][idx]
    prefix = "../" * this.count("/")

    def link(k):
        target = FILES[k][idx]
        href = prefix + target
        if href.endswith("index.html"):
            href = href[: -len("index.html")] or "./"
        return href

    other_lang = "de" if lang == "en" else "en"
    other_href = prefix + FILES[key][1 - idx]
    if other_href.endswith("index.html"):
        other_href = other_href[: -len("index.html")] or "./"

    nav = "".join(
        f'<li><a href="{link(k)}"{" aria-current=\"page\"" if k == key else ""}>{label}</a></li>'
        for k, label in NAV[lang]
    )
    lang_link = (f'<li><a class="lang" href="{other_href}" hreflang="{other_lang}" lang="{other_lang}" '
                 f'title="{UI[lang]["other_label"]}">{UI[lang]["other"]}</a></li>')
    title, desc = META[key][lang]
    body = CONTENT[key](lang, link)
    main_cls = "" if key == "home" else ' class="legal"'
    body_cls = "" if key == "home" else ' class="subpage"'
    home_href = link("home")

    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url(this)}">
<link rel="alternate" hreflang="en" href="{url(FILES[key][0])}">
<link rel="alternate" hreflang="de" href="{url(FILES[key][1])}">
<link rel="alternate" hreflang="x-default" href="{url(FILES[key][0])}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url(this)}">
<meta property="og:image" content="{BASE}assets/icon-1024.png">
<meta name="theme-color" content="#0f0224">
<link rel="icon" href="{prefix}assets/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{prefix}assets/icon-1024.png">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body{body_cls}>
<a class="skip" href="#main">{UI[lang]['skip']}</a>
{SCENE.format(p=prefix)}
<header class="site-header">
  <div class="bar">
    <a class="brand" href="{home_href}">{BRAND}</a>
    <nav class="site-nav" aria-label="Main"><ul>{nav}{lang_link}</ul></nav>
  </div>
</header>
<main id="main"{main_cls}>
{body}
</main>
<footer class="site-footer">
  <div class="bar">
    <nav class="site-nav" aria-label="Footer"><ul>{nav}{lang_link}</ul></nav>
    <p class="small">© 2026 vBADBULLv · {mailto()} · <a href="{REPO}">{UI[lang]['source']}</a></p>
    <p class="small">{UI[lang]['disclaimer']}</p>
  </div>
</footer>
</body>
</html>
"""


def main():
    written = []
    for key in FILES:
        for lang, idx in (("en", 0), ("de", 1)):
            out = ROOT / FILES[key][idx]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render(key, lang), encoding="utf-8")
            written.append(FILES[key][idx])

    urls = "\n".join(f"  <url><loc>{url(f)}</loc></url>" for f in written)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
    print("\n".join(url(f) for f in written))


if __name__ == "__main__":
    main()
