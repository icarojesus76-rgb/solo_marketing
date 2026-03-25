"""
================================================================================
🚀 FLOWCASH GLOBAL - ORQUESTRADOR PRINCIPAL DE MARKETING E VENDAS AI
================================================================================
Autor: FlowCash AI Team
Versão: 1.0.0
Descrição: Orquestrador global que coordena todas as Sub-Crews para executar
           campanhas de marketing, vendas e suporte 100% automatizados por IA.
================================================================================
"""

import os
import asyncio
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from crewai.tasks.task_output import TaskOutput

# ================================================================================
# CONFIGURAÇÃO DE API KEY
# ================================================================================

# Carregar variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# Verificar se a API key da OpenAI está configurada
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("⚠️  AVISO: OPENAI_API_KEY não encontrada no arquivo .env")
    print("   Por favor, configure sua API key para que os agentes possam funcionar.")
    print("   Crie um arquivo .env na raiz do projeto com: OPENAI_API_KEY=sua-chave")
    # Não bloqueamos a execução - os agentes ainda podem ser definidos

# ================================================================================
# IMPORTAÇÃO DOS AGENTES
# ================================================================================

# Adicionar o diretório agents ao path
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'agents'))

# Importar todos os agentes
try:
    from agents.orchestrador_global import (
        criar_agente_orchestrador,
        ORQUESTRADOR_SYSTEM_PROMPT
    )
    from agents.localizacao_cultural import (
        criar_agente_localizacao_cultural,
        AGENTE_LOCALIZACAO_SYSTEM_PROMPT
    )
    from agents.compliance import (
        criar_agente_compliance,
        AGENTE_COMPLIANCE_SYSTEM_PROMPT
    )
    from agents.inteligencia_cambial_preco import (
        criar_agente_inteligencia_cambial,
        AGENTE_CAMBIO_SYSTEM_PROMPT
    )
    from agents.traducao_contextual import (
        criar_agente_traducao,
        AGENTE_TRADUCAO_SYSTEM_PROMPT
    )
    from agents.pesquisa_conteudo_viral import (
        criar_agente_pesquisa_viral,
        AGENTE_PESQUISA_VIRAL_SYSTEM_PROMPT
    )
    from agents.roteiro_short_form import (
        criar_agente_roteiro_short_form,
        AGENTE_ROTEIRO_SHORT_SYSTEM_PROMPT
    )
    from agents.copys_legendas_social import (
        criar_agente_copys_legendas,
        AGENTE_COPYS_SYSTEM_PROMPT
    )
    from agents.design_visual_videomaker import (
        criar_agente_design_videomaker,
        AGENTE_DESIGN_SYSTEM_PROMPT
    )
    from agents.publicacao_calendario import (
        criar_agente_publicacao_calendario,
        AGENTE_CALENDARIO_SYSTEM_PROMPT
    )
    from agents.funil_vendas_global import (
        criar_agente_funil_vendas,
        AGENTE_FUNIL_SYSTEM_PROMPT
    )
    from agents.seo_blog import (
        criar_agente_seo_blog,
        AGENTE_SEO_SYSTEM_PROMPT
    )
    from agents.nurturing_email_whatsapp import (
        criar_agente_nurturing,
        AGENTE_NURTURING_SYSTEM_PROMPT
    )
    from agents.suporte_247 import (
        criar_agente_suporte,
        AGENTE_SUPORTE_SYSTEM_PROMPT
    )
    from agents.analise_sentimento_global import (
        criar_agente_sentimento,
        AGENTE_SENTIMENTO_SYSTEM_PROMPT
    )
    
    AGENTES_IMPORTADOS = True
    print("✅ Todos os agentes importados com sucesso!")
    
except ImportError as e:
    AGENTES_IMPORTADOS = False
    print(f"⚠️  Erro ao importar agentes: {e}")
    print("   Os agentes ainda serão criados com as definições padrão.")


# ================================================================================
# DEFINIÇÃO DE AGENTES (FALLBACK)
# ================================================================================

def criar_agentes_default():
    """
    Cria instâncias padrão dos agentes caso a importação falhe.
    """
    
    # Agente Orquestrador Global
    orquestrador = Agent(
        role="Orquestrador Global de Marketing e Vendas",
        goal="Coordenar todas as Sub-Crews para executar campanhas globais de marketing e vendas",
        backstory="""Você é o CEO virtual de marketing e vendas do FlowCash Global. 
        Com vasta experiência em marketing internacional B2B e operações de SaaS, você coordena 
        equipes de IA especializadas em diferentes funções e regiões do mundo. Sua missão é garantir 
        que todas as campanhas sejam executadas de forma coerente, eficiente e alinhada com os 
        objetivos estratégicos da empresa.""",
        verbose=True,
        allow_delegation=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Localização Cultural
    localizacao = Agent(
        role="Especialista em Localização Cultural",
        goal="Adaptar conteúdo para diferentes culturas e mercados",
        backstory="""Especialista em comunicação intercultural com foco em mercados 
        latino-americanos, europeus e norte-americanos. Conhece profundamente as nuances 
        culturais, expressões locais e contextos de negócios de cada região.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Compliance
    compliance = Agent(
        role="Especialista em Compliance e Regulamentações",
        goal="Garantir conformidade legal e ética em todas as comunicações",
        backstory="""Advogado digital especializado em LGPD, GDPR, CCPA e regulamentações 
        de proteção de dados. Garante que todas as comunicações de marketing e uso de 
        dados estejam em total conformidade com as leis locais.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Inteligência Cambial
    cambio = Agent(
        role="Especialista em Inteligência Cambial e Precificação",
        goal="Definir estratégias de precificação otimizadas para cada mercado",
        backstory="""Economista especializado em mercados emergentes e desenvolvidos. 
        Analisa poder de compra, câmbio e concorrência para definir planos de assinatura 
        competitivos e sustentáveis.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Tradução Contextual
    traducao = Agent(
        role="Tradutor Contextual Multilíngue",
        goal="Traduzir conteúdo financeiro com precisão técnica e fluidez",
        backstory="""Tradutor especializado em terminologia financeira e contábil. 
        Traduz conteúdos complexos mantendo a precisão técnica e a fluidez natural 
        de cada idioma.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Pesquisa de Conteúdo Viral
    pesquisa_viral = Agent(
        role="Pesquisador de Tendências Virais",
        goal="Identificar oportunidades de conteúdo viral em diferentes plataformas",
        backstory="""Especialista em análise de tendências de conteúdo digital. 
        Monitora padrões virais em TikTok, Reels, LinkedIn e YouTube para identificar 
        oportunidades de alcance orgânico de alto impacto.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Roteiro Short-Form
    roteiro = Agent(
        role="Roteirista de Conteúdo Curto",
        goal="Criar roteiros persuasivos para vídeos de 10-60 segundos",
        backstory="""Roteirista criativo especializado em conteúdo de formato curto. 
        Cria narrativas envolventes que capturam atenção nos primeiros segundos e 
        convertem visualizadores em leads.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Copys e Legendas
    copys = Agent(
        role="Copywriter e Criador de Legendas",
        goal="Escrever textos persuasivos para redes sociais e anúncios",
        backstory="""Copywriter especialista em vendas B2B e marketing digital. 
        Cria legendas, CTAs, hashtags e textos que engajam e convertem 
        o público-alvo de PMEs.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Design Visual / Videomaker
    design = Agent(
        role="Designer Visual e Videomaker",
        goal="Gerar prompts de IA para criação de imagens e vídeos otimizados",
        backstory="""Designer e videomaker especializado em conteúdo para redes sociais. 
        Cria prompts detalhados para ferramentas de IA generativa que resultam em 
        visuais profissionais e alinhados com a marca.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Publicação e Calendário
    calendario = Agent(
        role="Gestor de Publicação e Calendário Editorial",
        goal="Organizar e agendar publicações otimizadas por região e horário",
        backstory="""Gestor de conteúdo editorial com expertise em marketing de horários. 
        Define calendários de publicação otimizados para cada fuso horário e plataforma, 
        maximizando o alcance e engajamento.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Funil de Vendas
    funil = Agent(
        role="Arquiteto de Funil de Vendas",
        goal="Mapear e otimizar o funil de vendas completo",
        backstory="""Especialista em funis de vendas B2B e automação de marketing. 
        Desenha percursos de conversão eficientes do topo ao fundo do funil, 
        com estratégias de qualificação e nutrição de leads.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente SEO e Blog
    seo = Agent(
        role="Especialista em SEO e Conteúdo de Blog",
        goal="Criar conteúdo otimizado para SEO que atrai leads qualificados",
        backstory="""Especialista em marketing de conteúdo e SEO técnico. 
        Cria artigos educativos e otimizados para mecanismos de busca que atraem 
        PMEs em busca de soluções de gestão financeira.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Nurturing
    nurturing = Agent(
        role="Especialista em Nurturing e Nutrição de Leads",
        goal="Criar sequências de e-mail e WhatsApp que convertem leads",
        backstory="""Especialista em automação de marketing e nutrição de leads. 
        Cria sequências personalizadas que guiam leads pelo funil de vendas, 
        desde o primeiro contato até a assinatura.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Suporte 24/7
    suporte = Agent(
        role="Agente de Suporte 24/7",
        goal="Responder dúvidas sobre fluxo de caixa e produto em múltiplos idiomas",
        backstory="""Agente de suporte especializado em software financeiro para PMEs. 
        Fornece atendimento 24/7 em múltiplos idiomas, ajudando usuários com dúvidas 
        sobre fluxo de caixa, onboarding e uso do produto.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    # Agente Análise de Sentimento
    sentimento = Agent(
        role="Analista de Sentimento Global",
        goal="Monitorar e analisar percepção de marca e produto",
        backstory="""Analista de sentiment mining e business intelligence. 
        Monitora o que PMEs dizem sobre fluxo de caixa, competidores e o produto, 
        traduzindo insights em ações estratégicas de marketing e produto.""",
        verbose=True,
        llm="gpt-4o" if OPENAI_API_KEY else None
    )
    
    return {
        'orquestrador': orquestrador,
        'localizacao': localizacao,
        'compliance': compliance,
        'cambio': cambio,
        'traducao': traducao,
        'pesquisa_viral': pesquisa_viral,
        'roteiro': roteiro,
        'copys': copys,
        'design': design,
        'calendario': calendario,
        'funil': funil,
        'seo': seo,
        'nurturing': nurturing,
        'suporte': suporte,
        'sentimento': sentimento
    }


# ================================================================================
# DEFINIÇÃO DE TAREFAS
# ================================================================================

def criar_tarefas(agentes):
    """
    Cria as tarefas para cada agente.
    """
    
    tarefas = []
    
    # Tarefa 1: Análise de Mercado Global
    tarefa_analise = Task(
        description="""
        Realize uma análise completa do mercado global de gestão de fluxo de caixa para PMEs.
        
        Mercados-alvo:
        - Brasil (B2B SaaS em crescimento, PMEs familiares)
        - EUA (mercado maduro, automação financeira)
        - Europa (GDPR, múltiplas moedas)
        - México/LATAM (crescimento acelerado)
        
        Analise:
        1. Tamanho de mercado e potencial de crescimento
        2. Principais players e suas propostas de valor
        3. Oportunidades e ameaças de cada mercado
        4. Comportamento de compra típico das PMEs locais
        5. Barreiras de entrada e regulamentações
        
        Output esperado: Relatório de análise estratégica com recomendações.
        """,
        agent=agentes['orquestrador'],
        expected_output="Relatório completo de análise de mercado por região"
    )
    tarefas.append(tarefa_analise)
    
    # Tarefa 2: Definição de Estratégia de Precificação
    tarefa_preco = Task(
        description="""
        Defina a estratégia de precificação global para o FlowCash.
        
        Considere:
        - Poder de compra por país (PPP)
        - Câmbio atual e volatilidade
        - Estratégia de competidores
        - Custos operacionais locais
        
        Crie tabela de preços com:
        - 3-4 planos por mercado
        - Desconto por annual billing
        - Preços psicológicos eficientes
        - Comparativo de valor vs. competidores
        
        Output esperado: Tabela de precificação por mercado.
        """,
        agent=agentes['cambio'],
        expected_output="Estratégia de precificação com valores por mercado"
    )
    tarefas.append(tarefa_preco)
    
    # Tarefa 3: Criação de Calendário Editorial
    tarefa_calendario = Task(
        description="""
        Crie um calendário editorial mensal para todos os canais sociais.
        
        Canais:
        - Instagram (B2B brasileiro e latam)
        - TikTok (conteúdo viral sobre finanças)
        - LinkedIn (B2B profissional)
        - YouTube (tutoriais e explainers)
        
        Para cada dia do mês, defina:
        - Conteúdo a ser publicado
        - Formato (Reels, post, carrossel, vídeo)
        - Tema e objetivos
        - Hashtags principais
        
        Output esperado: Calendário editorial detalhado.
        """,
        agent=agentes['calendario'],
        expected_output="Calendário editorial mensal com 30 dias de conteúdo"
    )
    tarefas.append(tarefa_calendario)
    
    # Tarefa 4: Desenvolvimento de Funil de Vendas
    tarefa_funil = Task(
        description="""
        Desenvolva um funil de vendas completo para o FlowCash.
        
        Etapas do funil:
        1. Topo (TOFU) - Awareness
           - Anúncios educacionais
           - Conteúdo viral
           - SEO e blog
        
        2. Meio (MOFU) - Consideration
           - Webinars
           - Comparativos
           - Cases de sucesso
        
        3. Fundo (BOFU) - Decision
           - Trial gratuito
           - Demo personalizada
           - Consultoria gratuita
        
        Para cada etapa defina:
        - Canais de aquisição
        - Conteúdos necessários
        - Automações de nurturing
        - KPIs de acompanhamento
        - Scripts de abordagem
        
        Output esperado: Documento completo do funil de vendas.
        """,
        agent=agentes['funil'],
        expected_output="Funil de vendas end-to-end com automações"
    )
    tarefas.append(tarefa_funil)
    
    # Tarefa 5: Criação de Sequências de Nurturing
    tarefa_nurturing = Task(
        description="""
        Crie sequências de nurturing para cada estágio do funil.
        
        Sequences necessárias:
        
        1. Lead Frio (TOFU):
           - 5 e-mails ao longo de 14 dias
           - Foco em educação
        
        2. Lead Morno (MOFU):
           - 7 e-mails ao longo de 21 dias
           - Foco em diferenciação
        
        3. Lead Quente (BOFU):
           - 3 e-mails ao longo de 5 dias
           - Foco em conversão
        
        4. WhatsApp Sequence:
           - 4 mensagens para reengajar
           - Tom informal e direto
        
        Para cada e-mail/mensagem defina:
        - Assunto/prévia
        - Corpo do texto
        - CTA
        - Timing ideal
        
        Output esperado: Scripts completos de e-mail e WhatsApp.
        """,
        agent=agentes['nurturing'],
        expected_output="Sequências de nurturing para todos os estágios do funil"
    )
    tarefas.append(tarefa_nurturing)
    
    # Tarefa 6: Localização de Campanha
    tarefa_localizacao = Task(
        description="""
        Localize uma campanha de lançamento para o Brasil.
        
        Campanha original: "Simplifique seu fluxo de caixa e evite apertos no final do mês"
        
        Adapte para o mercado brasileiro:
        - Tom de voz (informal mas profissional)
        - Expressões regionais (caixa, faturamento, boleto)
        - Referências culturais locais
        - CTAs culturalmente relevantes
        - Conformidade com LGPD
        
        Output esperado: Campanha completa adaptada para Brasil.
        """,
        agent=agentes['localizacao'],
        expected_output="Campanha localizada com adaptações culturais e LGPD"
    )
    tarefas.append(tarefa_localizacao)
    
    # Tarefa 7: Análise de Sentimento
    tarefa_sentimento = Task(
        description="""
        Realize uma análise de sentimento do mercado de PMEs.
        
        Analise:
        1. O que PMEs estão dizendo sobre fluxo de caixa nas redes sociais?
        2. Quais são as principais dores mencionadas?
        3. O que estão dizendo sobre competidores?
        4. Qual a percepção geral sobre soluções SaaS?
        
        Identifique:
        - Palavras-chave mais mencionadas
        - Sentimentos predominantes (positivo/negativo/neutro)
        - Tendências emergentes
        - Oportunidades de conteúdo
        
        Output esperado: Relatório de análise de sentimento.
        """,
        agent=agentes['sentimento'],
        expected_output="Análise de sentimento com insights acionáveis"
    )
    tarefas.append(tarefa_sentimento)
    
    # Tarefa 8: Validação de Compliance
    tarefa_compliance = Task(
        description="""
        Valide a conformidade de todas as peças de marketing.
        
        Verifique:
        1. LGPD (Brasil):
           - Consentimento para coleta de dados
           - Política de privacidade acessível
           - Termos de uso claros
        
        2. GDPR (Europa):
           - Right to be forgotten
           - Portabilidade de dados
           - Base legal para processamento
        
        3. CCPA (EUA):
           - Opt-out de venda de dados
           - Divulgação de coleta
        
        4. Geral:
           - Sem promessas de rendimento
           - Isenções de responsabilidade adequadas
           - Linguagem acessível
        
        Output esperado: Relatório de compliance validado.
        """,
        agent=agentes['compliance'],
        expected_output="Relatório de conformidade para todos os mercados"
    )
    tarefas.append(tarefa_compliance)
    
    return tarefas


# ================================================================================
# CRIAÇÃO DA CREW PRINCIPAL
# ================================================================================

def criar_crew_principal():
    """
    Cria a crew principal com todos os agentes e tarefas.
    """
    
    # Obter agentes (importados ou default)
    if AGENTES_IMPORTADOS:
        agentes = {
            'orquestrador': criar_agente_orchestrador(),
            'localizacao': criar_agente_localizacao_cultural(),
            'compliance': criar_agente_compliance(),
            'cambio': criar_agente_inteligencia_cambial(),
            'traducao': criar_agente_traducao(),
            'pesquisa_viral': criar_agente_pesquisa_viral(),
            'roteiro': criar_agente_roteiro_short_form(),
            'copys': criar_agente_copys_legendas(),
            'design': criar_agente_design_videomaker(),
            'calendario': criar_agente_publicacao_calendario(),
            'funil': criar_agente_funil_vendas(),
            'seo': criar_agente_seo_blog(),
            'nurturing': criar_agente_nurturing(),
            'suporte': criar_agente_suporte(),
            'sentimento': criar_agente_sentimento()
        }
    else:
        agentes = criar_agentes_default()
    
    # Criar tarefas
    tarefas = criar_tarefas(agentes)
    
    # Criar crew com processo hierárquico
    crew = Crew(
        agents=list(agentes.values()),
        tasks=tarefas,
        process=Process.hierarchical,  # Orquestrador delega automaticamente
        manager_agent=agentes['orquestrador'],
        verbose=True,
        memory=True,  # Habilitar memória da crew
        embedder={
            "provider": "openai",
            "model": "text-embedding-3-small"
        }
    )
    
    return crew


# ================================================================================
# SUB-CREWS
# ================================================================================

def criar_subcrew_social():
    """
    Cria a Sub-Crew de Social Media.
    """
    
    agentes_social = [
        criar_agente_pesquisa_viral() if AGENTES_IMPORTADOS else Agent(
            role="Pesquisador de Tendências",
            goal="Identificar conteúdo viral",
            backstory="Especialista em tendências de redes sociais"
        ),
        criar_agente_roteiro_short_form() if AGENTES_IMPORTADOS else Agent(
            role="Roteirista",
            goal="Criar roteiros virais",
            backstory="Roteirista criativo"
        ),
        criar_agente_copys_legendas() if AGENTES_IMPORTADOS else Agent(
            role="Copywriter",
            goal="Escrever copys persuasivas",
            backstory="Copywriter B2B"
        ),
        criar_agente_design_videomaker() if AGENTES_IMPORTADOS else Agent(
            role="Designer",
            goal="Criar prompts visuais",
            backstory="Designer criativo"
        ),
        criar_agente_publicacao_calendario() if AGENTES_IMPORTADOS else Agent(
            role="Gestor de Calendário",
            goal="Organizar publicações",
            backstory="Gestor editorial"
        )
    ]
    
    tarefas_social = [
        Task(
            description="Pesquisar tendências de conteúdo viral sobre fluxo de caixa em TikTok, Reels e YouTube Shorts",
            agent=agentes_social[0],
            expected_output="Lista de 10 tendências virais com oportunidades"
        ),
        Task(
            description="Criar 5 roteiros de vídeos curtos (15-30s) baseados nas tendências identificadas",
            agent=agentes_social[1],
            expected_output="Roteiros prontos para gravação"
        ),
        Task(
            description="Escrever copys, legendas e hashtags para cada roteiro",
            agent=agentes_social[2],
            expected_output="Copys completas com CTAs"
        ),
        Task(
            description="Gerar prompts de IA para criação de thumbnails e capas de vídeo",
            agent=agentes_social[3],
            expected_output="Prompts otimizados para Midjourney/DALL-E"
        ),
        Task(
            description="Criar calendário semanal de publicações para Instagram, TikTok e LinkedIn",
            agent=agentes_social[4],
            expected_output="Calendário com horários otimizados"
        )
    ]
    
    crew_social = Crew(
        agents=agentes_social,
        tasks=tarefas_social,
        process=Process.sequential,
        verbose=True
    )
    
    return crew_social


def criar_subcrew_vendas():
    """
    Cria a Sub-Crew de Vendas e Funil.
    """
    
    agentes_vendas = [
        criar_agente_funil_vendas() if AGENTES_IMPORTADOS else Agent(
            role="Arquiteto de Funil",
            goal="Desenhar funil de vendas",
            backstory="Especialista em funis B2B"
        ),
        criar_agente_seo_blog() if AGENTES_IMPORTADOS else Agent(
            role="SEO Specialist",
            goal="Criar conteúdo SEO",
            backstory="Especialista em SEO"
        ),
        criar_agente_nurturing() if AGENTES_IMPORTADOS else Agent(
            role="Nurturing Expert",
            goal="Criar sequências de nutrição",
            backstory="Especialista em automação"
        )
    ]
    
    tarefas_vendas = [
        Task(
            description="Mapear funil completo do FlowCash com canais, automações e scripts",
            agent=agentes_vendas[0],
            expected_output="Funil de vendas documentado"
        ),
        Task(
            description="Criar 3 artigos de blog otimizados para SEO sobre fluxo de caixa",
            agent=agentes_vendas[1],
            expected_output="Artigos completos com meta tags"
        ),
        Task(
            description="Desenvolver sequências de e-mail e WhatsApp para cada estágio do funil",
            agent=agentes_vendas[2],
            expected_output="Sequências de nurturing completas"
        )
    ]
    
    crew_vendas = Crew(
        agents=agentes_vendas,
        tasks=tarefas_vendas,
        process=Process.sequential,
        verbose=True
    )
    
    return crew_vendas


def criar_subcrew_regional():
    """
    Cria a Sub-Crew Regional para um mercado específico.
    """
    
    agentes_regional = [
        criar_agente_localizacao_cultural() if AGENTES_IMPORTADOS else Agent(
            role="Localizador Cultural",
            goal="Adaptar para cultura local",
            backstory="Especialista em localização"
        ),
        criar_agente_compliance() if AGENTES_IMPORTADOS else Agent(
            role="Compliance Officer",
            goal="Garantir conformidade",
            backstory="Especialista legal"
        ),
        criar_agente_inteligencia_cambial() if AGENTES_IMPORTADOS else Agent(
            role="Pricing Analyst",
            goal="Definir preços locais",
            backstory="Economista"
        ),
        criar_agente_traducao() if AGENTES_IMPORTADOS else Agent(
            role="Tradutor",
            goal="Traduzir conteúdo",
            backstory="Tradutor especializado"
        )
    ]
    
    tarefas_regional = [
        Task(
            description="Adaptar mensagens e tom de voz para o mercado-alvo",
            agent=agentes_regional[0],
            expected_output="Guia de tom de voz local"
        ),
        Task(
            description="Validar conformidade com regulamentações locais (LGPD/GDPR/CCPA)",
            agent=agentes_regional[1],
            expected_output="Checklist de compliance"
        ),
        Task(
            description="Definir estratégia de precificação para o mercado local",
            agent=agentes_regional[2],
            expected_output="Tabela de preços local"
        ),
        Task(
            description="Traduzir todos os materiais de marketing para o idioma local",
            agent=agentes_regional[3],
            expected_output="Materiais traduzidos"
        )
    ]
    
    crew_regional = Crew(
        agents=agentes_regional,
        tasks=tarefas_regional,
        process=Process.sequential,
        verbose=True
    )
    
    return crew_regional


# ================================================================================
# EXECUÇÃO PRINCIPAL
# ================================================================================

def executar_crew_principal():
    """
    Executa a crew principal de marketing e vendas.
    """
    print("=" * 80)
    print("🚀 FLOWCASH GLOBAL - ORQUESTRADOR DE MARKETING E VENDAS AI")
    print("=" * 80)
    print()
    print(f"📅 Data de execução: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Verificar API Key
    if not OPENAI_API_KEY:
        print("⚠️  ATENÇÃO: Executando em modo demonstração (sem API key)")
        print("   Para ativar os agentes, configure OPENAI_API_KEY no arquivo .env")
        print()
    
    # Criar crew
    print("🔧 Criando crew de agentes...")
    crew = criar_crew_principal()
    print("✅ Crew criada com sucesso!")
    print()
    
    # Mostrar agentes e tarefas
    print(f"📊 Agentes na crew: {len(crew.agents)}")
    print(f"📋 Tarefas na crew: {len(crew.tasks)}")
    print()
    
    # Listar agentes
    print("👥 Agentes:")
    for i, agente in enumerate(crew.agents, 1):
        print(f"   {i}. {agente.role}")
    print()
    
    # Listar tarefas
    print("📝 Tarefas:")
    for i, tarefa in enumerate(crew.tasks, 1):
        print(f"   {i}. {tarefa.description[:60]}...")
    print()
    
    # Iniciar execução
    print("▶️  Iniciando execução da crew...")
    print("-" * 80)
    
    # Executar crew
    resultado = crew.kickoff()
    
    print("-" * 80)
    print()
    print("✅ Execução concluída!")
    print()
    print("📊 RESULTADO:")
    print(resultado)
    print()
    
    return resultado


def executar_subcrew_social():
    """
    Executa apenas a Sub-Crew de Social Media.
    """
    print("=" * 80)
    print("📱 FLOWCASH GLOBAL - SUB-CREW DE SOCIAL MEDIA")
    print("=" * 80)
    print()
    
    crew = criar_subcrew_social()
    resultado = crew.kickoff()
    
    return resultado


def executar_subcrew_vendas():
    """
    Executa apenas a Sub-Crew de Vendas.
    """
    print("=" * 80)
    print("💰 FLOWCASH GLOBAL - SUB-CREW DE VENDAS")
    print("=" * 80)
    print()
    
    crew = criar_subcrew_vendas()
    resultado = crew.kickoff()
    
    return resultado


def executar_subcrew_regional(mercado="Brasil"):
    """
    Executa a Sub-Crew Regional para um mercado específico.
    """
    print("=" * 80)
    print(f"🌍 FLOWCASH GLOBAL - SUB-CREW REGIONAL ({mercado.upper()})")
    print("=" * 80)
    print()
    
    crew = criar_subcrew_regional()
    resultado = crew.kickoff()
    
    return resultado


# ================================================================================
# MENU INTERATIVO
# ================================================================================

def menu_principal():
    """
    Exibe menu interativo para seleção de execução.
    """
    
    while True:
        print()
        print("=" * 80)
        print("🚀 FLOWCASH GLOBAL - MENU DE EXECUÇÃO")
        print("=" * 80)
        print()
        print("Selecione uma opção:")
        print()
        print("1. 🚀 Executar Crew Principal (Marketing + Vendas completo)")
        print("2. 📱 Executar Sub-Crew Social Media")
        print("3. 💰 Executar Sub-Crew Vendas")
        print("4. 🌍 Executar Sub-Crew Regional (Brasil)")
        print("5. 🌍 Executar Sub-Crew Regional (EUA)")
        print("6. 🌍 Executar Sub-Crew Regional (Europa)")
        print("7. 📋 Listar agentes e tarefas")
        print("8. ❌ Sair")
        print()
        
        opcao = input("Digite o número da opção: ").strip()
        print()
        
        if opcao == "1":
            executar_crew_principal()
        elif opcao == "2":
            executar_subcrew_social()
        elif opcao == "3":
            executar_subcrew_vendas()
        elif opcao == "4":
            executar_subcrew_regional("Brasil")
        elif opcao == "5":
            executar_subcrew_regional("EUA")
        elif opcao == "6":
            executar_subcrew_regional("Europa")
        elif opcao == "7":
            listar_agentes_tarefas()
        elif opcao == "8":
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


def listar_agentes_tarefas():
    """
    Lista todos os agentes e tarefas disponíveis.
    """
    print()
    print("=" * 80)
    print("📋 LISTA DE AGENTES E TAREFAS")
    print("=" * 80)
    print()
    
    agentes = criar_agentes_default()
    
    print("👥 AGENTES DISPONÍVEIS:")
    print("-" * 80)
    for i, (nome, agente) in enumerate(agentes.items(), 1):
        print(f"   {i:2}. {nome.upper()}")
        print(f"       Role: {agente.role}")
        print(f"       Goal: {agente.goal}")
        print()
    
    print("📝 TAREFAS DISPONÍVEIS:")
    print("-" * 80)
    tarefas = criar_tarefas(agentes)
    for i, tarefa in enumerate(tarefas, 1):
        print(f"   {i}. {tarefa.description[:70]}..." if len(tarefa.description) > 70 else f"   {i}. {tarefa.description}")
        print(f"      Agent: {tarefa.agent.role}")
        print()


# ================================================================================
# PONTO DE ENTRADA
# ================================================================================

if __name__ == "__main__":
    import sys
    
    # Verificar argumentos de linha de comando
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()
        
        if comando == "principal" or comando == "full":
            executar_crew_principal()
        elif comando == "social":
            executar_subcrew_social()
        elif comando == "vendas":
            executar_subcrew_vendas()
        elif comando == "brasil":
            executar_subcrew_regional("Brasil")
        elif comando == "eua" or comando == "usa":
            executar_subcrew_regional("EUA")
        elif comando == "europa" or comando == "eu":
            executar_subcrew_regional("Europa")
        elif comando == "lista" or comando == "list":
            listar_agentes_tarefas()
        elif comando == "help":
            print("""
🚀 FLOWCASH GLOBAL - Comandos disponíveis:

  python main.py principal   - Executar crew principal completa
  python main.py social      - Executar sub-crew de social media
  python main.py vendas      - Executar sub-crew de vendas
  python main.py brasil      - Executar sub-crew para Brasil
  python main.py eua         - Executar sub-crew para EUA
  python main.py europa      - Executar sub-crew para Europa
  python main.py lista       - Listar agentes e tarefas
  python main.py help        - Mostrar esta ajuda

Sem argumentos: Inicia menu interativo.
""")
        else:
            print(f"❌ Comando '{comando}' não reconhecido. Use 'python main.py help'")
    else:
        # Modo interativo
        menu_principal()
