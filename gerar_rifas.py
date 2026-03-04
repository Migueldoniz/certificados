"""
Gerador de Rifas Numeradas
Gera um único PDF com todas as rifas numeradas sobre uma imagem de template.

Uso:
    python gerar_rifas.py

Configure as variáveis abaixo antes de executar.
"""

from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import os
import sys
import tempfile
import shutil

# ============================================================
# CONFIGURAÇÃO — EDITE AQUI
# ============================================================

# Caminho da imagem do template da rifa
TEMPLATE = "template_rifa.png"

# Intervalo de números
NUMERO_INICIO = 1
NUMERO_FIM = 200

# Formato do número (ex: "Nº 001")
PREFIXO = "Nº "
DIGITOS = 3  # quantidade de dígitos (001, 002, etc.)

# Fonte do número
# A Rajdhani NÃO suporta o caractere "º", por isso usamos Arial
# Para usar outra fonte TTF, altere o caminho abaixo
FONTE = "arial.ttf"

# Posição 1
POS1_X = 538
POS1_Y = 575
POS1_TAMANHO = 57
POS1_COR = (0, 0, 0)

# Posição 2
POS2_X = 1012
POS2_Y = 82
POS2_TAMANHO = 57
POS2_COR = (0, 0, 0)

# Nome do PDF de saída
PDF_SAIDA = "rifas.pdf"

# ============================================================
# FIM DA CONFIGURAÇÃO
# ============================================================


def formatar_numero(n):
    return f"{PREFIXO}{str(n).zfill(DIGITOS)}"


def carregar_fonte(tamanho):
    try:
        font = ImageFont.truetype(FONTE, tamanho, encoding='unic')
        return font
    except (OSError, IOError):
        print(f"⚠️  Fonte '{FONTE}' não encontrada, usando Arial.")
        try:
            return ImageFont.truetype("arial.ttf", tamanho, encoding='unic')
        except (OSError, IOError):
            return ImageFont.load_default()


def main():
    # Verificar template
    if not os.path.exists(TEMPLATE):
        print(f"❌ Template não encontrado: {TEMPLATE}")
        print(f"   Coloque a imagem do template na pasta do projeto com o nome '{TEMPLATE}'")
        print(f"   Ou altere a variável TEMPLATE no script.")
        sys.exit(1)

    # Carregar template e fontes
    template = Image.open(TEMPLATE).convert("RGB")
    largura, altura = template.size
    print(f"📐 Template: {largura}x{altura}px")

    fonte1 = carregar_fonte(POS1_TAMANHO)
    fonte2 = carregar_fonte(POS2_TAMANHO)

    total = NUMERO_FIM - NUMERO_INICIO + 1
    print(f"🎟️  Gerando {total} rifas ({NUMERO_INICIO} a {NUMERO_FIM})...")

    # Criar pasta temporária para as imagens
    temp_dir = tempfile.mkdtemp()

    try:
        # Criar PDF
        pdf = FPDF(unit="pt", format=(largura * 72 / 96, altura * 72 / 96))
        pdf.set_auto_page_break(False)

        for i in range(NUMERO_INICIO, NUMERO_FIM + 1):
            # Copiar template
            img = template.copy()
            draw = ImageDraw.Draw(img)

            texto = formatar_numero(i)

            # Desenhar número na posição 1
            draw.text((POS1_X, POS1_Y), texto, fill=POS1_COR, font=fonte1)

            # Desenhar número na posição 2
            draw.text((POS2_X, POS2_Y), texto, fill=POS2_COR, font=fonte2)

            # Salvar imagem temporária
            temp_path = os.path.join(temp_dir, f"rifa_{i}.jpg")
            img.save(temp_path, "JPEG", quality=95)

            # Adicionar ao PDF
            pdf.add_page()
            pdf.image(temp_path, 0, 0, largura * 72 / 96, altura * 72 / 96)

            # Progresso
            progresso = i - NUMERO_INICIO + 1
            pct = progresso / total * 100
            print(f"\r   [{progresso}/{total}] {pct:.0f}%", end="", flush=True)

        print()  # Nova linha após progresso

        # Salvar PDF
        pdf.output(PDF_SAIDA)
        tamanho_mb = os.path.getsize(PDF_SAIDA) / (1024 * 1024)
        print(f"✅ PDF gerado: {PDF_SAIDA} ({tamanho_mb:.1f} MB)")
        print(f"   {total} páginas, resolução: {largura}x{altura}px")

    finally:
        # Limpar ficheiros temporários
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
