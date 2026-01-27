## FairTradeConect – Plataforma de Certificação e Comércio Confiável
"Transparência que certifica, confiança que conecta o campo ao mercado.".

## 1. IDENTIDADE E APRESENTAÇÃO

Tecnologias: Python 3.12+ | Django 6.0.

## 1.1 Escopo do projeto
O projeto busca solucionar a dificuldade existente na relação entre microprodutores e pequenas empresas, especialmente na falta de confiança, transparência e validação de qualidade dos produtos comercializados. Atualmente, o processo de cadastramento e certificação não se conecta ao mercado, o que reduz a credibilidade e o valor percebido pelos compradores. O objetivo é desenvolver uma solução que torne esse processo mais seguro, transparente e acessível.

## 1.2 Descrição da Solução (MVP)
A solução proposta é o desenvolvimento do FairTradeConect, uma plataforma que permite o cadastro de produtores, empresas e produtos, além de um fluxo digital de certificação, no qual documentos são enviados, avaliados e aprovados ou rejeitados pelo administrador. O sistema também permitirá o acompanhamento das etapas da produção e a geração automática de anúncios de produtos certificados, simulando sua publicação em marketplaces. O MVP entregará as funcionalidades essenciais para validar o conceito de certificação e comércio confiável.

## 2. Modelagem de Dados e Planejamento do FairTradeConect
A Sprint 1 tem foco na modelagem do banco de dados e no planejamento inicial do MVP. Nesta etapa, serão criados o Sprint Backlog detalhado, o modelo conceitual de dados (DER), o modelo lógico (tabelas e relações), a definição da stack tecnológica e o cronograma das entregas.

## 2.1. Sprint Backlog
O Sprint Backlog é a lista de todas as tarefas que a equipe planeja executar nesta sprint. Cada tarefa foi dividida em subtarefas claras, com responsáveis atribuídos e estimativas de esforço. As tarefas são priorizadas segundo sua importância para o MVP e organizadas pelas dependências (tarefas que devem preceder outras). Exemplos de tarefas planejadas:
• Definição de Requisitos e User Stories (prioridade alta): Detalhar as funcionalidades do MVP (cadastro de produtor, empresa, produto, envio de documentos, fluxo de certificação) com critérios de aceitação claros. Esta tarefa depende do escopo do projeto já definido.
• Configuração do Ambiente de Desenvolvimento (alta): Criar repositório Git/GitHub e quadro Trello, instalar Python/Django, e configurar banco de dados (MySQL). As subtarefas incluem inicializar o projeto Django, instalar bibliotecas e configurar acesso ao banco, sendo um pré-requisito para implementar o backend.
• Modelagem de Dados Conceitual (alta): Identificar entidades principais (Produtor, Produto, Documento, Certificação, Empresa, Administrador) e seus atributos. Desenhar o Diagrama Entidade-Relacionamento definindo os relacionamentos entre elas. Por exemplo, cada Produtor cadastrado pode oferecer vários Produtos (relação 1:N), e cada Administrador pode avaliar várias Certificações (relação 1:N). Subtarefas incluem listar atributos de cada entidade e determinar cardinalidades.
• Modelagem de Dados Lógico (média): Traduzir o modelo conceitual em tabelas relacionais. Definir cada tabela (nome, atributos e tipo de dados) com chave primária e chaves estrangeiras correspondentes. Por exemplo, a tabela Produto terá FK para Produtor (produtor_id). Cada entidade converte-se em tabela, cada uma com uma chave primária única, dependendo do modelo conceitual.
• Implementação Inicial do Banco de Dados (média): Criar as migrations Django ou scripts SQL para as tabelas definidas. Certificar que as restrições de integridade (PK/FK) estejam corretas para garantir consistência referencial.
• Desenvolvimento Backend Básico (média): Implementar as classes models do Django para Produtor, Produto, etc., de acordo com o modelo lógico. Criar endpoints ou views iniciais para inserção e consulta de dados, dependendo do ambiente configurado e das tabelas criadas.
• Definição de Stack Tecnológica (média): Listar as linguagens, frameworks, bibliotecas e ferramentas a serem usadas, dependendo do levantamento das necessidades do MVP.
• Planejamento de MVP e Cronograma (baixa): Detalhar as funcionalidades do MVP e distribuir as entregas pelas semanas seguintes. Criar o cronograma de atividades e os critérios de sucesso para refinar o escopo e orientar o backlog.
• Atualização do Quadro de Tarefas (Trello/GitHub): Registrar todas as tarefas acima no quadro Kanban, atribuindo responsáveis e estimativas. Priorizar tarefas de alto impacto e de acordo com as dependências, garantindo que cada tarefa tenha um responsável claro para evitar sobreposição.

## 2.3. Modelo Conceitual (DER)
No Modelo Conceitual (Diagrama Entidade-Relacionamento) definimos as entidades principais do domínio e como elas se relacionam. As entidades identificadas foram:
• Produtor: Representa o microprodutor, possuindo atributos como id_produtor, nome, CPF/CNPJ, contato, endereço e histórico de certificações.
• Produto: Representa o produto oferecido pelo produtor, com id_produto, nome, descrição, categoria e data de produção.
• Documento: Refere-se a arquivos ou formulários enviados pelo produtor para certificação, contendo id_documento, tipo (PDF, imagem), data_envio e status (pendente, aprovado, reprovado).
• Certificação: Registra o resultado da avaliação de qualidade, incluindo id_certificacao, data_certificacao, validade e status (concluída, expirado).
• Empresa: Representa a pequena empresa interessada nos produtos certificados, com id_empresa, nome, CNPJ, contato e endereço.
• Administrador: Usuário do sistema com privilégios de avaliação, possuindo id_adm, nome, login e senha.
As relações principais definidas são:
• Produtor ↔ Produto (1:N): Um Produtor pode oferecer vários Produtos; cada Produto pertence a um único Produtor.
• Produtor ↔ Documento (1:N): Um Produtor envia vários Documentos para certificação; cada Documento é enviado por exatamente um Produtor.
• Produto ↔ Certificação (1:1): Cada Produto certificado possui uma única entrada em Certificação.
• Administrador ↔ Certificação (1:N): Um Administrador pode avaliar muitas Certificações, mas cada Certificação é avaliada por um único Administrador.
• Empresa ↔ Produto (N:M, futura evolução): Opcionalmente, uma Empresa pode se relacionar a vários Produtos e vice-versa, o que exigiria uma entidade associativa.
As regras do diagrama garantem a integridade e adequação do modelo ao contexto do comércio confiável do FairTradeConect.

## 2.4 Modelo Lógico
O Modelo Lógico descreve como as entidades do DER viram tabelas relacionais no banco de dados. Cada entidade torna-se uma tabela com chave primária única, contendo colunas correspondentes aos atributos e chaves estrangeiras para relacionamentos.
Tabelas Sugeridas:
Tabela
Atributos (tipo)
PK
FKs
Produtor
id_produtor (INT), nome (VARCHAR), cpf_cnpj (CHAR), endereço (VARCHAR), email (VARCHAR), telefone (VARCHAR)
id_produtor
–
Produto
id_produto (INT), nome (VARCHAR), descricao (TEXT), categoria (VARCHAR), data_producao (DATE), produtor_id (INT)
id_produto
produtor_id → Produtor(id_produtor)
Documento
id_documento (INT), tipo (VARCHAR), descricao (TEXT), data_envio (DATE), status (VARCHAR), produtor_id (INT)
id_documento
produtor_id → Produtor(id_produtor)
Certificacao
id_certificacao (INT), produto_id (INT), administrador_id (INT), data_certificacao (DATE), validade (DATE), status (VARCHAR)
id_certificacao
produto_id → Produto(id_produto); administrador_id → Administrador(id_adm)
Empresa
id_empresa (INT), nome (VARCHAR), cnpj (CHAR), endereco (VARCHAR), email (VARCHAR), telefone (VARCHAR)
id_empresa
–
Administrador
id_adm (INT), nome (VARCHAR), email (VARCHAR), senha (VARCHAR)
id_adm
–
Cada produto cadastrado guarda em produtor_id a referência ao Produtor responsável, assim como cada documento. A tabela Certificacao relaciona produto_id e administrador_id às respectivas tabelas para registrar quem aprovou e quando. As chaves estrangeiras asseguram consistência referencial conforme a modelagem conceitual.

## 3. Stack Tecnológica
A stack escolhida prioriza ferramentas maduras para acelerar a construção do MVP:
• Linguagem de Programação – Python: Versátil, de alto nível e com sintaxe concisa para desenvolvimento rápido e legível.
• Framework Backend – Django: Framework web “batteries included” que oferece recursos integrados como autenticação, painel admin e ORM. É projetado para levar aplicações do conceito à produção rapidamente, focando em segurança e escalabilidade.
• Biblioteca API – Django REST Framework (DRF): Estende o Django para criar APIs RESTful de forma simples, permitindo gerar endpoints de CRUD rapidamente.
• Frontend – React.js: Biblioteca ideal para interfaces interativas com componentes reutilizáveis e desempenho eficiente via virtual DOM.
• Banco de Dados – SQLITE3: Escolhido por sua fácil integração com Django, ampla comunidade e escalabilidade inicial.
• Outras Ferramentas: Git/GitHub para versão, Trello para gerenciamento ágil, VS Code como IDE, Postman para testes de APIs e Docker (opcional) para containers.

## 4. Planejamento da Sprint 1
Entregáveis: Espera-se ter prontos o Sprint Backlog, o cronograma do MVP, o DER, o modelo lógico e a definição da stack tecnológica. Estes artefatos formam a base para o primeiro incremento funcional na Semana 3.
Responsabilidades por membro:
• Samuel Fernandes (Product Owner, Dev Team): Definição e priorização das User Stories; validação de requisitos e escopo; revisão de tarefas; documentação da arquitetura e suporte na configuração do banco.
• Danielle Santa Brigida (Scrum Master, Dev Team): Coordenação de reuniões; manutenção do quadro Trello; remoção de impedimentos; liderança técnica na modelagem de dados (DER e modelo lógico).
• Peter Wesley (Dev Team): Configuração do ambiente (Django, banco); implementação inicial dos models e migrações; criação de endpoints básicos para cadastro/consulta.
Dificuldades Previstas e Mitigação:
• Escopo e requisitos pouco claros: Mitigado pelo refinamento do backlog e histórias de usuário antes da sprint.
• Dependências ocultas: Mitigado pelo mapeamento antecipadamente da ordem das tarefas e uso de ferramentas visuais.
• Recursos limitados: Mitigado por estudos rápidos, pair programming e documentação de decisões.
• Mudanças de prioridades: Mitigado pela limitação de alterações durante a sprint e revisões rápidas do backlog.

## 5. GUIA DE INSTALAÇÃO
Para configurar o ambiente e rodar a aplicação localmente, utilize os seguintes comandos:
1. Clone o repositório: git clone https://github.com/Samuel-Fernandes1010/FairTradeConect2.0
2. Instale as dependências necessárias: pip install asgiref==3.11.0 Django==6.0 sqlparse==0.5.5 tzdata==2025.3 Pillow==12.1.0
3. Execute as migrações para criar o banco de dados automático (SQLite3): python manage.py makemigrations python manage.py migrate
4. Inicie o servidor de desenvolvimento: python manage.py runserver

## 6. LINKS OFICIAIS
• Repositório GitHub: https://github.com/Samuel-Fernandes1010/FairTradeConect2.0
• Quadro de Gestão Ágil (Trello): https://trello.com/invite/b/69221ddc701f5732f5ddc266/ATTI4e231d2d74e8e39c150aabd27a36e38fF7C763AF/projeto-integrador-comercio-justo
• Pasta de Documentação Complementar e Vídeo (Google Drive): https://drive.google.com/drive/folders/1I2AyY405KoSm-0OvdGsQ08WFenDVW1n3 https://drive.google.com/file/d/1kkCOI9fECKE2DrRC86hPRQIz3w6kcF6H/view?usp=sharing

## 7. EQUIPE BETA
• Danielle Santa Brígida – Scrum Master, Dev Team
• Samuel Gomes Fernandes – Product Owner, Dev Team
• Petter Wesley – Dev Team
