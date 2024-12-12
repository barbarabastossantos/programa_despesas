from fpdf import FPDF
import calendar
from datetime import datetime
import locale

# Configurar o padrão de localização para formato de moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Função para gerar o PDF
def gerar_pdf(despesas, nome_arquivo_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adiciona o título
    pdf.cell(200, 10, "Relatório do Mês", ln=True, align="C")
    pdf.ln(10)  # Adiciona espaço

    # Adiciona o mês e o ano
    hoje = datetime.now()
    mes = calendar.month_name[hoje.month]
    ano = hoje.year
    pdf.cell(200, 10, f"Mês: {mes} {ano}", ln=True, align="C")
    pdf.ln(10)

    # Adiciona as despesas
    for despesa in despesas:
        data, descricao, valor = despesa
        linha = f"Data: {data} | Descrição: {descricao} | Valor: {locale.currency(valor, grouping=True)}"
        pdf.multi_cell(0, 10, linha)

    # Salva o arquivo
    pdf.output(nome_arquivo_pdf)
    print(f"PDF gerado com sucesso: {nome_arquivo_pdf}")


# Função principal
def registrar_despesas():
    despesas = []

    while True:
        try:
            data = input("Digite a data (DD/MM/AAAA) ou 'fim' para terminar o mês: ").strip()
            if data.lower() == 'fim':
                break

            # Valida formato da data
            datetime.strptime(data, "%d/%m/%Y")

            descricao = input("Digite a descrição da despesa: ").strip()
            valor = float(input("Digite o valor da despesa: R$").replace(",", "."))

            despesas.append((data, descricao, valor))
        except ValueError:
            print("Entrada inválida! Certifique-se de que a data e o valor estão corretos.")

    if despesas:
        nome_arquivo_pdf = f"relatorio_despesas_{calendar.month_name[datetime.now().month]}{datetime.now().year}.pdf".replace(" ", "")
        gerar_pdf(despesas, nome_arquivo_pdf)
    else:
        print("Nenhuma despesa registrada.")


# Executar
registrar_despesas()
