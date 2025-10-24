import ollama


def test_ollama_stream():
    model_name = "mistral:7b"
    prompt = "Scrie 'Salut!' și adaugă un mic mesaj de bun venit."

    try:
        print("🤖 Test Ollama (streaming)...")
        response_stream = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        # Iterează și afișează output-ul pe măsură ce vine
        for chunk in response_stream:
            if 'content' in chunk:
                print(chunk['content'], end='', flush=True)

        print("\n✅ Streaming complet!")

    except Exception as e:
        print("❌ Eroare la conectarea cu Ollama:")
        print(e)


if __name__ == "__main__":
    test_ollama_stream()
