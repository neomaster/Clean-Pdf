Este script em Python permite remover palavras, frases e CPFs de arquivos PDF sem alterar o fundo ou layout visual.



🔹 Como usar no Windows

Abra o Prompt de Comando (cmd) ou PowerShell.

Execute:

python limpar_pdfs.py


Digite as instruções no prompt conforme solicitado:

Informe os caminhos dos PDFs (separados por vírgula): "C:\Users\SeuNome\Documentos\contrato.pdf","C:\Users\SeuNome\Documentos\relatorio.pdf"
Palavras/frases para remover (separadas por vírgula): confidencial,teste
Marcas a remover (separadas por vírgula): rascunho
Remover CPFs automaticamente? (s/n): s

📌 Resultado:

Para cada PDF informado, gera um novo arquivo com sufixo _limpo.pdf na mesma pasta.

Exemplo:

contrato.pdf → contrato_limpo.pdf

relatorio.pdf → relatorio_limpo.pdf

📂 Exemplo de Saída

Se você tiver:

C:\Users\User\Documentos\contrato.pdf

C:\Users\User\Documentos\relatorio.pdf

O script vai gerar:

C:\Users\User\Documentos\contrato_limpo.pdf

C:\Users\User\Documentos\relatorio_limpo.pdf

⚠️ Observações Importantes

O script não sobrescreve os arquivos originais.

Para processar múltiplos arquivos, separe os caminhos por vírgula.

Se a opção de CPF estiver habilitada, ele removerá tanto CPFs no formato 000.000.000-00 quanto os de 11 dígitos contínuos.

Caso um arquivo não seja encontrado ou ocorra erro, o script exibirá no final uma lista de erros.


          ／＞　 フ
         | 　_　_| 
      ／` ミ＿xノ 
     /　　　　 |
    /　 ヽ　　 ﾉ
   │　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_ヽ_)__)
＼二)

🗡️ SAMURAI 🗡️
