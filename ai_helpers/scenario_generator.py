import ollama
import os


def genereaza_scenariu_gherkin(descriere_functionalitate):
    """
    Generează un scenariu Gherkin pe baza unei descrieri în limba română
    """

    prompt = f"""
Ești un expert în testare automată și Gherkin/BDD.

Generează UN singur scenariu de test în format Gherkin pentru această funcționalitate:
{descriere_functionalitate}

Folosește structura:
Feature: [nume feature]

  Scenario: [nume scenariu descriptiv]
    Given [precondiție]
    When [acțiune utilizator]
    Then [rezultat așteptat]

IMPORTANT: 
- Scrie în limba română
- UN SINGUR scenariu, nu mai multe
- Fără explicații sau text suplimentar
- Doar codul Gherkin
"""

    response = ollama.chat(
        model='mistral:7b',
        messages=[{'role': 'user', 'content': prompt}],
        options={'temperature': 0.3}
    )

    return response['message']['content']


def salveaza_scenariu(scenariu, nume_fisier):
    """
    Salvează scenariul într-un fișier .feature
    """
    output_dir = 'output/scenarios'
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, nume_fisier)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(scenariu)

    print(f"✅ Scenariu salvat: {filepath}")


# Test rapid
if __name__ == "__main__":
    print("🚀 Generez scenariu de test...\n")

    scenariu = genereaza_scenariu_gherkin(
        "Utilizatorul se autentifică cu username și parolă corectă"
    )

    print("📝 Scenariu generat:")
    print("=" * 60)
    print(scenariu)
    print("=" * 60)

    salveaza_scenariu(scenariu, 'login_success.feature')