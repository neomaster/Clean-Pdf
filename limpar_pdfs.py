import fitz  # PyMuPDF
import re
import os

def remove_from_pdf(pdf_path, output_path, phrases, marks, remove_cpf=True):
    doc = fitz.open(pdf_path)
    cpf_regex = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b")

    try:
        for page in doc:
            terms = [p.strip() for p in (phrases + marks) if p.strip()]

            # Remover termos digitados
            for term in terms:
                for area in page.search_for(term):
                    page.add_redact_annot(area, text="", fill=None)

            # Remover CPFs automaticamente
            if remove_cpf:
                for match in cpf_regex.finditer(page.get_text("text")):
                    cpf = match.group()
                    for area in page.search_for(cpf):
                        page.add_redact_annot(area, text="", fill=None)

            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)

        doc.save(output_path, deflate=True, garbage=4)
    finally:
        doc.close()


def main():
    print("=== Remover Texto de PDFs (Windows Prompt) ===\n")

    arquivos = input("Informe os caminhos dos PDFs (separados por vírgula): ").split(",")
    frases = input("Palavras/frases para remover (separadas por vírgula): ").split(",")
    marcas = input("Marcas a remover (separadas por vírgula): ").split(",")
    remove_cpf = input("Remover CPFs automaticamente? (s/n): ").strip().lower() != "n"

    arquivos = [a.strip('" ').strip() for a in arquivos if a.strip()]

    if not arquivos:
        print("Nenhum arquivo informado. Encerrando.")
        return

    erros = []
    for arquivo in arquivos:
        try:
            if not os.path.exists(arquivo):
                raise FileNotFoundError("Arquivo não encontrado.")

            pasta = os.path.dirname(arquivo) or "."
            nome = os.path.splitext(os.path.basename(arquivo))[0]
            saida = os.path.join(pasta, f"{nome}_limpo.pdf")

            remove_from_pdf(arquivo, saida, frases, marcas, remove_cpf)
            print(f"[OK] {arquivo} → {saida}")
        except Exception as e:
            erros.append(f"{arquivo}: {e}")

    if erros:
        print("\n[ERROS]")
        for erro in erros:
            print(erro)
    else:
        print("\nTodos os PDFs foram processados com sucesso!")


if __name__ == "__main__":
    main()
