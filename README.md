# 🎓 Gerador de Certificados & 🎟️ Rifas

Ferramentas para gerar certificados e rifas numeradas em PDF, com envio automático por email.

## Certificados

1. Abra `index.html` no browser
2. Edite o texto do certificado e a lista de nomes no script
3. Defina a imagem de fundo (descomente `background-image` no `style.css`)
4. Os PDFs são gerados automaticamente

### Envio por Email

```bash
# Configure as variáveis de ambiente
set EMAIL=seu_email@gmail.com
set SENHA=sua_senha_de_app

# Execute o script
python script/enviar.py
```

Os dados dos participantes ficam em `script/participantes.csv`.

## Rifas Numeradas

### 1. Posicionar os números (visual)

1. Abra `rifa.html` no browser
2. Carregue a imagem do template da rifa
3. **Arraste os 2 números** para a posição desejada
4. Copie as coordenadas geradas automaticamente (bloco "Copie para o gerar_rifas.py")

### 2. Gerar o PDF (Python)

1. Cole as coordenadas no topo do `gerar_rifas.py`
2. Coloque a imagem do template como `template_rifa.png` na raiz do projeto
3. Execute:

```bash
pip install Pillow fpdf2
python gerar_rifas.py
```

O ficheiro `rifas.pdf` será gerado com todas as rifas numeradas (1 página por número).

### Configuração (`gerar_rifas.py`)

| Variável | Descrição |
|----------|-----------|
| `TEMPLATE` | Caminho da imagem do template |
| `NUMERO_INICIO` / `NUMERO_FIM` | Intervalo de números (ex: 1 a 200) |
| `PREFIXO` | Texto antes do número (ex: `Nº `) |
| `DIGITOS` | Zeros à esquerda (3 → `001`) |
| `FONTE` | Fonte TTF (padrão: `arial.ttf`) |
| `POS1_X`, `POS1_Y`, `POS1_TAMANHO`, `POS1_COR` | Posição, tamanho e cor do número 1 |
| `POS2_X`, `POS2_Y`, `POS2_TAMANHO`, `POS2_COR` | Posição, tamanho e cor do número 2 |

> **Nota:** A fonte Rajdhani não suporta o caractere `º`. Use `arial.ttf` ou outra fonte que suporte.

## Estrutura

```
├── index.html            # Gerador de certificados
├── style.css             # Estilos dos certificados
├── rifa.html             # Ferramenta visual de posicionamento
├── rifa-style.css        # Estilos da ferramenta de rifas
├── gerar_rifas.py        # Gerador de rifas em PDF (Python)
├── template_rifa.png     # Imagem do template da rifa
├── Fonte/                # Fontes Rajdhani
├── lib/                  # Bibliotecas JS (jsPDF, html2canvas)
├── script/
│   ├── enviar.py         # Script de envio por email
│   └── participantes.csv
├── .env.example          # Template de variáveis de ambiente
└── .gitignore
```
