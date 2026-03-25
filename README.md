# 🚀 FlowCash Global - Orquestrador de Marketing e Vendas AI

<div align="center">

![FlowCash](https://img.shields.io/badge/FlowCash-Global-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge)
![CrewAI](https://img.shields.io/badge/CrewAI-1.11.1-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Sistema de marketing e vendas 100% automatizado por IA para gestão de fluxo de caixa B2B**

*15+ agentes de IA cooperando para executar campanhas globais de marketing, vendas e suporte*

</div>

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Arquitetura de Agentes](#arquitetura-de-agentes)
- [Mercados Alvo](#mercados-alvo)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [KPIs e Métricas](#kpis-e-métricas)
- [Roadmap](#roadmap)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## 🎯 Visão Geral

O **FlowCash Global** é um SaaS B2B revolucionário focado em **gestão de fluxo de caixa para PMEs**, operando com **100% de automação por IA**.

### Objetivos Estratégicos (3 Anos)

| Fase | Meta | Timeline |
|------|------|----------|
| **MVP** | Lançamento no Brasil com 100 clientes | Mês 1-6 |
| **Expansão LATAM** | México, Colombia, Argentina | Mês 6-12 |
| **Expansão Global** | EUA, Europa, APAC | Mês 12-24 |
| **Liderança** | MRR de $1M+ em múltiplos mercados | Mês 24-36 |

### Problema que Resolvemos

```
😰 Dificuldade de prever fluxo de caixa
😰 Apertos de caixa no final do mês
😰 Falta de visibilidade entre receitas e despesas
😰 Dependência de planilhas manuais e desatualizadas
😰 Decisões financeiras baseadas em dados inconsistentes
```

### Nossa Solução

```
✅ Visualização em tempo real do fluxo de caixa
✅ Previsões automatizadas de receitas e despesas
✅ Alertas inteligentes de紧绷 de caixa
✅ Integração com bancos e sistemas contábeis
✅ Relatórios automáticos para tomada de decisão
```

---

## 🤖 Arquitetura de Agentes

### Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ORQUESTRADOR GLOBAL                               │
│                  (Coordena todas as Sub-Crews e Campanhas)                 │
└─────────────────────────────────────────────────────────────────────────────┘
                    │                    │                    │
          ┌─────────┴─────────┐ ┌─────────┴─────────┐ ┌─────┴─────┐
          │   SUB-CREW       │ │   SUB-CREW       │ │ SUB-CREW  │
          │   REGIONAL       │ │   SOCIAL         │ │ VENDAS    │
          │                  │ │                  │ │           │
          │ • Localização    │ │ • Pesquisa Viral │ │ • Funil   │
          │ • Compliance     │ │ • Roteiros       │ │ • SEO     │
          │ • Câmbio/Preço   │ │ • Copys          │ │ • Nurture │
          │ • Tradução       │ │ • Design          │ │           │
          │                  │ │ • Calendário     │ │           │
          └─────────┬─────────┘ └─────────┬─────────┘ └─────┬─────┘
                    │                    │                  │
                    └────────────────────┼──────────────────┘
                                        │
                              ┌─────────┴─────────┐
                              │   SUB-CREW        │
                              │   SUPORTE 24/7    │
                              │                   │
                              │ • Suporte Técnico │
                              │ • Análise Sent.   │
                              └───────────────────┘
```

### Lista de Agentes

| ID | Agente | Função | Mercados |
|----|--------|--------|----------|
| 01 | **Orquestrador Global** | Coordena todas as crews e campanhas | Global |
| 02 | **Localização Cultural** | Adapta conteúdo para cada cultura | BR, US, EU, MX |
| 03 | **Compliance** | Valida LGPD, GDPR, CCPA | BR, US, EU |
| 04 | **Inteligência Cambial** | Define preços por mercado | BR, US, EU, MX |
| 05 | **Tradução Contextual** | Traduz conteúdo técnico | Todos |
| 06 | **Pesquisa Viral** | Identifica tendências de conteúdo | Global |
| 07 | **Roteiro Short-Form** | Cria roteiros para Reels/TikTok | Global |
| 08 | **Copys & Legendas** | Escreve textos persuasivos | Todos |
| 09 | **Design/Videomaker** | Gera prompts visuais | Global |
| 10 | **Calendário Editorial** | Organiza publicações | Global |
| 11 | **Funil de Vendas** | Desenha percursos de conversão | Global |
| 12 | **SEO/Blog** | Cria conteúdo otimizado | Global |
| 13 | **Nurturing** | Cria sequências de nutrição | Global |
| 14 | **Suporte 24/7** | Atendimento multilíngue | Todos |
| 15 | **Análise Sentimento** | Monitora percepção de marca | Global |

---

## 🌍 Mercados Alvo

### Brasil 🇧🇷
- **Segmento**: PMEs familiares, startups, prestadores de serviço
- **Canais**: Instagram, WhatsApp, LinkedIn
- **Preço**: R$ 97-297/mês (PPP otimizado)
- **Compliance**: LGPD
- **Tensão**: "Apertos de caixa no final do mês"

### Estados Unidos 🇺🇸
- **Segmento**: SMBs, agências, consultorias
- **Canais**: LinkedIn, YouTube, Google Ads
- **Preço**: $29-99/mês
- **Compliance**: CCPA, SOC2
- **Tensão**: "Falta de visibilidade em múltiplas contas"

### Europa 🇪🇺
- **Segmento**: KMEs (Pequenas e Médias Empresas)
- **Canais**: LinkedIn, YouTube, TikTok
- **Preço**: €25-85/mês
- **Compliance**: GDPR, DSA
- **Tensão**: "Gestão multicurrency complexa"

### México/LATAM 🌎
- **Segmento**: PYMES, comerciantes, manufatura leve
- **Canais**: WhatsApp, Instagram, TikTok
- **Preço**: MX$ 399-1,199/mês
- **Compliance**: LFPDPPP (México)
- **Tensão**: "Incerteza de receita semanal"

---

## 📦 Pré-requisitos

- **Python**: 3.11 ou superior
- **API Key OpenAI**: Para powered by GPT-4o
- **Git**: Para controle de versão
- **8GB RAM**: Mínimo recomendado
- **20GB Disco**: Para dependências e dados

---

## 🔧 Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/icarojesus76-rgb/solo_marketing.git
cd solo_marketing
```

### 2. Crie o Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

Ou instale diretamente:

```bash
pip install crewai python-dotenv
```

### 4. Configure as Variáveis de Ambiente

```bash
# Copie o arquivo de exemplo
copy .env.example .env

# Edite o .env com suas chaves de API
notepad .env
```

### 5. Configure sua API Key

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-4o
```

---

## ⚙️ Configuração

### Estrutura do .env

```env
# API Keys
OPENAI_API_KEY=sk-...           # Obrigatório
OPENAI_MODEL=gpt-4o             # Opcional (padrão: gpt-4o)

# CRM (Opcional)
HUBSPOT_API_KEY=your-key        # Opcional

# Marketing (Opcional)
SENDGRID_API_KEY=SG...          # Opcional
TWILIO_ACCOUNT_SID=...          # Opcional
```

### Ambientes

| Variável | Valor | Descrição |
|-----------|-------|-----------|
| `ENVIRONMENT` | `development` | Modo desenvolvimento |
| `ENVIRONMENT` | `staging` | Homologação |
| `ENVIRONMENT` | `production` | Produção |
| `LOG_LEVEL` | `DEBUG` | Detalhado |
| `LOG_LEVEL` | `INFO` | Padrão |
| `LOG_LEVEL` | `ERROR` | Mínimo |

---

## 🚀 Uso

### Execução Completa (Crew Principal)

```bash
python main.py principal
```

### Execução por Sub-Crew

```bash
# Social Media
python main.py social

# Vendas
python main.py vendas

# Regional Brasil
python main.py brasil

# Regional EUA
python main.py eua

# Regional Europa
python main.py europa
```

### Menu Interativo

```bash
python main.py
```

Saída:
```
🚀 FLOWCASH GLOBAL - MENU DE EXECUÇÃO

1. Executar Crew Principal
2. Executar Sub-Crew Social
3. Executar Sub-Crew Vendas
4. Executar Sub-Crew Regional (Brasil)
5. Executar Sub-Crew Regional (EUA)
6. Executar Sub-Crew Regional (Europa)
7. Listar agentes e tarefas
8. Sair
```

### Listar Agentes

```bash
python main.py lista
```

### Ajuda

```bash
python main.py help
```

---

## 📁 Estrutura do Projeto

```
solo_marketing/
├── 📄 README.md                    # Este arquivo
├── 📄 requirements.txt            # Dependências Python
├── 📄 .env.example                 # Template de configuração
├── 📄 .gitignore                   # Arquivos ignorados
│
├── 📄 main.py                      # Orquestrador principal
├── 📄 PLANO_MARKETING.md          # Plano de marketing completo
├── 📄 context.md                  # Contexto do projeto
│
├── 📁 agents/                     # Agentes CrewAI
│   ├── 01_orchestrador_global.py
│   ├── 02_localizacao_cultural.py
│   ├── 03_compliance.py
│   ├── 04_inteligencia_cambial_preco.py
│   ├── 05_traducao_contextual.py
│   ├── 06_pesquisa_conteudo_viral.py
│   ├── 07_roteiro_short_form.py
│   ├── 08_copys_legendas_social.py
│   ├── 09_design_visual_videomaker.py
│   ├── 10_publicacao_calendario.py
│   ├── 11_funil_vendas_global.py
│   ├── 12_seo_blog.py
│   ├── 13_nurturing_email_whatsapp.py
│   ├── 14_suporte_247.py
│   └── 15_analise_sentimento_global.py
│
└── 📁 configs/                   # Configurações
    └── crew_config.py            # Configuração da crew
```

---

## 📊 KPIs e Métricas

### Marketing

| KPI | Meta Mensal | Descrição |
|-----|-------------|-----------|
| **Tráfego Orgânico** | +25% MoM | Crescimento de visitantes únicos |
| **Leads Qualificados (MQL)** | 500+ | Leads prontos para vendas |
| **CPL (Custo por Lead)** | <$15 | Eficiência de aquisição |
| **Taxa Conversão Site→Lead** | >3% | Eficiência de conversão |
| **Engajamento Social** | +20% | Likes, comments, shares |

### Vendas

| KPI | Meta Mensal | Descrição |
|-----|-------------|-----------|
| **Conversão MQL→SQL** | >25% | Qualificação de leads |
| **Taxa Conversão Trial→Pay** | >10% | Eficiência de conversão |
| **Lead Time** | <48h | Tempo até primeiro contato |
| **MRR** | +15% MoM | Receita recorrente mensal |
| **CAC** | <$150 | Custo de aquisição de cliente |

### Produto & Suporte

| KPI | Meta Mensal | Descrição |
|-----|-------------|-----------|
| **NPS** | >50 | Satisfação do cliente |
| **Churn Rate** | <3% | Taxa de cancelamento |
| **Tempo Resposta Suporte** | <4h | SLA de atendimento |
| **CSAT** | >85% | Satisfação com suporte |

---

## 🗺️ Roadmap

### Fase 1: MVP (Meses 1-6)
- [x] Arquitetura de agentes
- [x] Crew principal configurada
- [x] Funil de vendas Brasil
- [ ] Integração CRM
- [ ] Landing page com SEO
- [ ] 100 primeiros clientes

### Fase 2: Expansão LATAM (Meses 6-12)
- [ ] Localização México
- [ ] Localização Colombia
- [ ] Calendário editorial multilíngue
- [ ] Campanhas pagas regionais
- [ ] 1,000 clientes LATAM

### Fase 3: Globalização (Meses 12-24)
- [ ] Localização EUA
- [ ] Localização Europa
- [ ] Sistema de pricing dinâmico
- [ ] 10,000 clientes globais
- [ ] MRR $100K+

### Fase 4: Liderança (Meses 24-36)
- [ ] Agentes especializados por vertical
- [ ] Previsões de IA avançadas
- [ ] Integrações bancárias globais
- [ ] MRR $1M+
- [ ] IPO Preparation

---

## 🤝 Contribuição

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Add nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Padrões de Código

- Follow PEP 8
- Docstrings em português
- Tipos definidos para parâmetros
- Testes unitários obrigatórios

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Contato

<div align="center">

**FlowCash AI Team**

[![GitHub](https://img.shields.io/badge/GitHub-icarojesus76--rgb-blue?style=flat-square)](https://github.com/icarojesus76-rgb)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-FlowCash-blue?style=flat-square)](https://linkedin.com/company/flowcash)

*Transformando a gestão financeira de PMEs com inteligência artificial*

</div>
