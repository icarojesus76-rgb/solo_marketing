# CONTEXTO GLOBAL DO PROJETO
## SaaS B2B de Fluxo de Caixa para PMEs - Escala Global

**Versão:** 2.0  
**Data:** 25 de março de 2026  
**Última Atualização:** Com agentes CrewAI e estrutura completa  

---

## 1. VISÃO DE NEGÓCIO (3 ANOS)

### 1.1 Missão
Transformar a gestão financeira de PMEs globalmente através de inteligência artificial acessível e intuitiva.

### 1.2 Objetivos Estratégicos

| Horizonte | MRR Alvo | Mercados | Meta |
|-----------|----------|----------|------|
| **Ano 1** | R$ 500K | Brasil (piloto) | MVP + product-market fit |
| **Ano 2** | R$ 2.5M | Brasil + EUA | Escala e automação |
| **Ano 3** | R$ 10M+ | Global | Líder de mercado |

### 1.3 Pilares Estratégicos

1. **Educação como aquisição** - Conteúdo que resolve problemas reais
2. **Automação completa** - Agentes IA operam 24/7
3. **Localization-first** - Comunicação culturalmente relevante
4. **Product-led growth** - Trial gratuito com conversão orgânica
5. **Parcerias estratégicas** - Ecossistema de contadores como canal

---

## 2. PÚBLICO-ALVO

### 2.1 Segmentação Primária

PMEs com faturamento anual entre R$ 360 mil e R$ 50 milhões.

**Setores:**
- Varejo e Comércio (38%)
- Serviços profissionais (27%)
- Indústria e manufatura (18%)
- Alimentação e hospitality (12%)
- Tecnologia e startups (5%)

### 2.2 Personas

| ID | Persona | Perfil | Dor Principal |
|----|---------|--------|---------------|
| PER-001 | O Dono Prático | Proprietário, 35-55 anos | Sem visibilidade do caixa |
| PER-002 | A Controladora | CFO/Controller, 30-50 anos | Reconciliação manual |
| PER-003 | O Contador | Escritório contábil | Diferenciação de mercado |

### 2.3 Pontos de Dor Comuns

- 60% das PMEs fecham por falta de controle de caixa
- 82% das falências связаны с má gestão financeira
- 73% dos donos admitem não entender o fluxo de caixa
- 15h/semana gastas em reconciliação manual

---

## 3. ARQUITETURA DE AGENTES (CREWAI)

### 3.1 Estrutura Hierárquica

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ARQUITETURA DE AGENTES                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              ORQUESTRADOR GLOBAL                                  │   │
│  │              (AGENT-001)                                          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                               │                                         │
│         ┌─────────────────────┼─────────────────────┐                   │
│         ▼                     ▼                     ▼                   │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐            │
│  │   REGIONAL  │      │   SOCIAL    │      │   VENDAS    │            │
│  │  SUB-CREW   │      │  SUB-CREW   │      │  SUB-CREW   │            │
│  └─────────────┘      └─────────────┘      └─────────────┘            │
│         │                     │                     │                   │
│         ▼                     ▼                     ▼                   │
│  • Localização      • Pesquisa Viral      • Funil Global               │
│  • Compliance       • Roteiros           • SEO Blog                   │
│  • Preço/Câmbio     • Copys/Social       • Nurturing                  │
│  • Tradução         • Design/Video       • Calendário                  │
│                     • Publicação                                       │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    SUPORTE SUB-CREW                               │   │
│  │  • Suporte 24/7              • Análise de Sentimento             │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Lista de Agentes

| ID | Agente | Função | Sub-Crew |
|----|--------|--------|----------|
| AGENT-001 | Orquestrador Global | Coordenação de campanhas | Principal |
| AGENT-002 | Localização Cultural | Adaptação cultural | Regional |
| AGENT-003 | Compliance | LGPD/GDPR/CCPA | Regional |
| AGENT-004 | Inteligência Cambial/Preço | Estratégia de pricing | Regional |
| AGENT-005 | Tradução Contextual | Tradução multilíngue | Regional |
| AGENT-006 | Pesquisa Conteúdo Viral | Tendências de conteúdo | Social |
| AGENT-007 | Roteiro Short-Form | Scripts para Reels/TikTok | Social |
| AGENT-008 | Copys/Legendas Social | Copywriting para redes | Social |
| AGENT-009 | Design Visual/Videomaker | Prompts para IA generativa | Social |
| AGENT-010 | Publicação/Calendário | Programação de posts | Social |
| AGENT-011 | Funil de Vendas Global | Mapeamento de funil | Vendas |
| AGENT-012 | SEO/Blog | Conteúdo otimizado | Vendas |
| AGENT-013 | Nurturing E-mail/WhatsApp | Sequências de nutrição | Vendas |
| AGENT-014 | Suporte 24/7 | Atendimento automatizado | Suporte |
| AGENT-015 | Análise Sentimento | Social listening | Suporte |

### 3.3 Fluxo de Dependências

```
ORQUESTRADOR (AGENT-001)
    │
    ├── REGIONAL SUB-CREW
    │   ├── Localização (2) ──► Tradução (5) ──► Compliance (3)
    │   └── Preço (4)
    │
    ├── SOCIAL SUB-CREW
    │   ├── Pesquisa Viral (6) ──► Roteiro (7) ──► Copys (8)
    │   ├── Design (9) ──► Publicação (10)
    │   └── Calendário (10)
    │
    ├── VENDAS SUB-CREW
    │   ├── Funil (11) ──► SEO (12)
    │   ├── Nurturing (13)
    │   └── Calendário (10)
    │
    └── SUPORTE SUB-CREW
        ├── Suporte 24/7 (14)
        └── Sentimento (15) ──► Orquestrador (feedback)
```

---

## 4. KPIs GLOBAIS

### 4.1 KPIs de Negócio

| KPI | Definição | Meta Ano 1 | Meta Ano 2 | Meta Ano 3 |
|-----|-----------|------------|------------|------------|
| MRR | Receita recorrente mensal | R$ 500K | R$ 2.5M | R$ 10M |
| CAC | Custo de aquisição | < R$ 180 | < R$ 150 | < R$ 120 |
| LTV | Valor do cliente lifetime | R$ 3.6K | R$ 6K | R$ 9.6K |
| LTV:CAC | Ratio de eficiência | > 2.0x | > 3.0x | > 4.0x |
| Churn | Taxa de cancelamento | < 3% | < 2.5% | < 2% |

### 4.2 KPIs de Marketing

| KPI | Meta Ano 1 | Meta Ano 2 | Meta Ano 3 |
|-----|------------|------------|------------|
| Leads/mês | 1.250 | 4.000 | 15.000 |
| Tráfego único/mês | 33.000 | 120.000 | 500.000 |
| NPS | > 45 | > 55 | > 65 |

### 4.3 KPIs de Automação IA

| KPI | Meta Ano 1 | Meta Ano 2 | Meta Ano 3 |
|-----|------------|------------|------------|
| Leads processados por IA | 60% | 80% | 90% |
| Respostas IA (suporte) | 50% | 70% | 85% |
| Conteúdo gerado por IA | 40% | 60% | 80% |

---

## 5. MERCADOS E EXPANSÃO

### 5.1 Roadmap de Expansão

| Fase | Período | Mercados | Estratégia |
|------|---------|----------|------------|
| 1 | Q1-Q2 2026 | Brasil | MVP, product-market fit |
| 2 | Q3-Q4 2026 | Brasil + México | Escala LATAM |
| 3 | 2027 | EUA | Escala NA |
| 4 | 2027-2028 | Europa (PT/ES/DE/FR) | Escala EMEA |
| 5 | 2028+ | APAC | Escala global |

### 5.2 Estrutura de Preços por Mercado

| Mercado | Moeda | Plano Starter | Plano Pro | Plano Enterprise |
|---------|-------|--------------|-----------|-----------------|
| Brasil | BRL | R$ 97 | R$ 197 | R$ 497 |
| EUA | USD | $29 | $59 | $149 |
| Europa | EUR | €25 | €49 | €129 |
| México | MXN | $149 | $299 | $799 |

---

## 6. REQUISITOS TÉCNICOS

### 6.1 Stack de Tecnologia

- **Orquestração**: CrewAI
- **Automação**: n8n / Zapier
- **CRM**: HubSpot / Pipedrive
- **Analytics**: Google Analytics 4, Mixpanel
- **Email**: SendGrid / Mailchimp
- **WhatsApp**: Twilio / Z-API
- **Armazenamento**: AWS S3 / GCP
- **Compliance**: LGPD, GDPR, CCPA ready

### 6.2 Integrações Prioritárias

- +200 bancos conectados
- Principais ERPs (SAP, TOTVS, D365)
- Ferramentas contábeis
- Gateways de pagamento

---

## 7. COMPLIANCE E SEGURANÇA

### 7.1 Framework de Compliance

| Região | Regulamento | Status |
|--------|-------------|--------|
| Brasil | LGPD | ✓ Implementado |
| Europa | GDPR | ✓ Implementado |
| EUA (CA) | CCPA | ✓ Implementado |

### 7.2 Princípios de Ética de IA

- Transparência no uso de IA
- Ausência de viés algorítmico
- Respeito à privacidade
- Human-in-the-loop para decisões críticas

---

## 8. ESTRUTURA DE DIRETÓRIOS

```
MARKETING/
├── agents/                    # Agentes CrewAI
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
├── tasks/                     # Tasks CrewAI
│   └── [tasks correspondentes]
│
├── workflows/                 # Automação (n8n/Zapier)
│   ├── workflow_analise_tendencias_virais.py
│   ├── workflow_funil_vendas_global.py
│   ├── workflow_posts_virais_auto.py
│   └── workflow_nurturing_leads.py
│
├── knowledge/                  # Base de conhecimento
│   └── [prompts e documentação]
│
├── configs/                    # Configurações
│   └── crew_config.py
│
├── examples/                   # Exemplos de conteúdo
│   ├── reels/
│   ├── meta_ads/
│   ├── google_ads/
│   ├── linkedin/
│   ├── blog/
│   ├── email/
│   ├── whatsapp/
│   └── landing_page/
│
├── context.md                  # Contexto original
├── context.2.md                # Este documento
└── PLANO_MARKETING_SAAS_B2B_FLUXO_CAIXA.md
```

---

## 9. PRÓXIMOS PASSOS

### 9.1 Fase 1 - MVP (Meses 1-3)

- [ ] Implementar Orquestrador Global (AGENT-001)
- [ ] Implementar Sub-Crew Regional básica
- [ ] Implementar Sub-Crew Social básica
- [ ] Configurar primeiro funil Brasil
- [ ] Lançar site com trial gratuito

### 9.2 Fase 2 - Escala (Meses 4-6)

- [ ] Expandir todos os agentes
- [ ] Configurar automações completas
- [ ] Lançar em mercado piloto
- [ ] Implementar análise de sentimento
- [ ] Configurar suporte 24/7

### 9.3 Fase 3 - Expansão (Meses 7-12)

- [ ] Escalar para México e EUA
- [ ] Otimizar baseado em dados
- [ ] Expandir integrações
- [ ] Preparar lançamento Europa

---

**Documento vivo - Atualizar conforme evolução do projeto.**
