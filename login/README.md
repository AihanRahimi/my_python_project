# Login System (Python)

Ein einfaches Login-System, das ich zur Vertiefung meiner Python-Kenntnisse entwickelt habe.

## Funktionen
- Registrierung neuer Benutzer (Sign Up)
- Login mit Benutzername und Passwort
- Passwörter werden mit SHA-256 gehasht gespeichert (keine Klartext-Passwörter)
- Begrenzung der Login-Versuche (3 Versuche, danach temporäre Sperre)
- Interaktives Menü zur Auswahl der Funktionen

## Verwendete Technologien
- Python 3
- hashlib für Passwort-Hashing
- Dateibasierte Speicherung (user.txt)

## Installation & Ausführung
`bash
python login.py