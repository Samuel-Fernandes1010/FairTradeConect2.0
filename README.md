-------------------------------------------------------------------------------
# FairTradeConect – Plataforma de Certificação e Comércio Confiável
> **"Transparência que certifica, confiança que conecta o campo ao mercado."**

![Status do Projeto](https://img.shields.io/badge/Status-Sprint%204%20Conclu%C3%ADda-green)
![Python Version](https://img.shields.io/badge/Python-3.12+-blue)
![Django Version](https://img.shields.io/badge/Django-6.0-092e20)

## 1. Identidade e Apresentação
O **FairTradeConect** busca solucionar a dificuldade existente na relação entre microprodutores e pequenas empresas (PMEs), focando na **falta de confiança, transparência e validação de qualidade** dos produtos comercializados. Atualmente, a ausência de um processo de certificação acessível reduz a credibilidade e o valor percebido pelos compradores. Nossa solução automatiza o fluxo de certificação digital, tornando esse processo mais seguro e transparente.

---

## 2. Evidências Visuais
A plataforma foi desenhada para oferecer um fluxo intuitivo de validação de produtos.

### Caminho da Aplicação 
1.  **Cadastramento:** Registro de perfis para Produtores Rurais, Empresas e Administradores.
2.  **Mapeamento e Listagem:** Organização e categorização de produtos naturais para visualização organizada na plataforma.
3.  **Processo de Certificação (Autodeclaração):** O produtor envia fotos, ficha técnica e notas fiscais para assegurar a procedência do produto.
4.  **Auditoria Admin:** Um usuário **Admin** avalia as evidências enviadas para aprovar ou reprovar o "selo de qualidade inicial" da Amazônia Marketing & Consultoria.
5.  **Monitoramento Logístico:** Atualização manual dos status de venda como "Em estoque", "Disponível" e "Esgotado".

---

## 3. Detalhes Técnicos

### Funcionalidades Implementadas (Checklist MVP)
- [x] **Cadastramento e Mapeamento (Prioridade 1):** Registro completo de produtores e empresas com listagem organizada de produtos.
- [x] **Fluxo de Certificação Digital:** Sistema autodeclaratório com suporte para envio de documentos e fotos.
- [x] **Acompanhamento da Logística:** Controle de status de venda e etapas da produção.
- [x] **Painel de Auditoria (Admin):** Interface para validação de certificados por responsáveis técnicos.


### Stack Tecnológica
*   **Linguagem:** Python (versatilidade e codificação rápida).
*   **Framework Backend:** Django 6.0 e Django REST Framework (DRF).
*   **Banco de Dados:** **SQLite3** (conforme configurado nativamente no Django para este projeto).
*   **Processamento de Imagem:** Pillow 12.1.0 (essencial para manipulação de fotos de certificação).
*   **Frontend:** React.js (interfaces interativas e componentes reutilizáveis).
*   **Requisitos Adicionais:** asgiref==3.11.0, sqlparse==0.5.5, tzdata==2025.3.

---

## 4. Guia de Instalação
Siga os comandos abaixo para configurar o ambiente e rodar a aplicação localmente:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Samuel-Fernandes1010/FairTradeConect2.0
    ```
2.  **Instale as dependências necessárias:**
    ```bash
    pip install asgiref==3.11.0 Django==6.0 sqlparse==0.5.5 tzdata==2025.3 Pillow==12.1.0
    ```
3.  **Execute as migrações para criar o banco de dados automático (SQLite3):**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

---

## 5. Links Oficiais

**Equipe Beta (Dev Team):**
*   **Danielle Santa Brígida** – Scrum Master, Dev Team.
*   **Samuel Gomes Fernandes** – Product Owner, Dev Team.
*   **Petter Wesley** – Dev Team (Responsável pela configuração do ambiente e implementação inicial).

### Links Oficiais do Projeto
*   **Repositório GitHub:** https://github.com/Samuel-Fernandes1010/FairTradeConect2.0
*   **Quadro de Gestão Ágil (Trello):** https://trello.com/invite/b/69221ddc701f5732f5ddc266/ATTI4e231d2d74e8e39c150aabd27a36e38fF7C763AF/projeto-integrador-comercio-justo
*   **Pasta de Documentação Complementar e Vídeo (Drive):** https://drive.google.com/drive/folders/1I2AyY405KoSm-0OvdGsQ08WFenDVW1n3

**Licença:** MIT.
