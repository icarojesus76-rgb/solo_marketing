"""
Configuração Principal da Crew - SaaS B2B Fluxo de Caixa
========================================================

Arquivo de configuração central para orchestration da crew de agentes
de marketing e vendas global.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Crew, Process
from agents.01_orchestrador_global import OrquestradorGlobalAgent
from agents.02_localizacao_cultural import LocalizacaoCulturalAgent
from agents.03_compliance import ComplianceAgent
from agents.04_inteligencia_cambial_preco import InteligenciaCambialPrecoAgent
from agents.05_traducao_contextual import TraducaoContextualAgent
from agents.06_pesquisa_conteudo_viral import PesquisaConteudoViralAgent
from agents.07_roteiro_short_form import RoteiroShortFormAgent
from agents.08_copys_legendas_social import CopysLegendasSocialAgent
from agents.09_design_visual_videomaker import DesignVisualVideomakerAgent
from agents.10_publicacao_calendario import PublicacaoCalendarioAgent
from agents.11_funil_vendas_global import FunilVendasGlobalAgent
from agents.12_seo_blog import SEOBlogAgent
from agents.13_nurturing_email_whatsapp import NurturingEmailWhatsappAgent
from agents.14_suporte_247 import Suporte247Agent
from agents.15_analise_sentimento_global import AnaliseSentimentoGlobalAgent
from tasks import (
    orchestrador_global_task,
    localizacao_cultural_task,
    compliance_task,
    inteligencia_cambial_task,
    traducao_contextual_task,
    pesquisa_viral_task,
    roteiro_short_form_task,
    copys_social_task,
    design_visual_task,
    publicacao_calendario_task,
    funil_vendas_task,
    seo_blog_task,
    nurturing_task,
    suporte_247_task,
    analise_sentimento_task
)
from typing import Dict, List, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MarketingCrew:
    """
    Crew principal de marketing e vendas para o SaaS de Fluxo de Caixa.
    
    Estrutura da Crew:
    - Orquestrador Global (coordena todas as sub-crews)
    - Sub-Crew Regional (localização, compliance, pricing)
    - Sub-Crew Social (conteúdo viral, roteiros, copys)
    - Sub-Crew Vendas (funil, SEO, nurturing)
    - Sub-Crew Suporte (suporte 24/7, análise de sentimento)
    """
    
    def __init__(self):
        self.config = self._carregar_config()
        self.agentes = {}
        self.tasks = {}
        
    def _carregar_config(self) -> Dict:
        """Carrega configuração global."""
        return {
            "nome": "Marketing Crew - Fluxo de Caixa SaaS",
            "versao": "1.0.0",
            "mercados": ["BR", "US", "EU", "MX", "APAC"],
            "idiomas": ["pt-BR", "en-US", "es-ES", "de-DE", "fr-FR"],
            "moedas": ["BRL", "USD", "EUR", "MXN"],
            "timezone_default": "America/Sao_Paulo",
            "compliance_frameworks": ["LGPD", "GDPR", "CCPA"]
        }
    
    def inicializar_agentes(self) -> Dict[str, Any]:
        """
        Inicializa todos os agentes da crew.
        
        Returns:
            Dict: Dicionário de agentes inicializados
        """
        logger.info("Inicializando agentes da crew...")
        
        # Inicializar agentes
        self.agentes = {
            "orquestrador": OrquestradorGlobalAgent().criar_agente(),
            "localizacao": LocalizacaoCulturalAgent().criar_agente(),
            "compliance": ComplianceAgent().criar_agente(),
            "preco": InteligenciaCambialPrecoAgent().criar_agente(),
            "traducao": TraducaoContextualAgent().criar_agente(),
            "pesquisa_viral": PesquisaConteudoViralAgent().criar_agente(),
            "roteiro": RoteiroShortFormAgent().criar_agente(),
            "copys": CopysLegendasSocialAgent().criar_agente(),
            "design": DesignVisualVideomakerAgent().criar_agente(),
            "calendario": PublicacaoCalendarioAgent().criar_agente(),
            "funil": FunilVendasGlobalAgent().criar_agente(),
            "seo": SEOBlogAgent().criar_agente(),
            "nurturing": NurturingEmailWhatsappAgent().criar_agente(),
            "suporte": Suporte247Agent().criar_agente(),
            "sentimento": AnaliseSentimentoGlobalAgent().criar_agente()
        }
        
        logger.info(f"Agentes inicializados: {len(self.agentes)}")
        return self.agentes
    
    def criar_crew(self) -> Crew:
        """
        Cria a crew completa com todos os agentes e tasks.
        
        Returns:
            Crew: Crew configurada e pronta para execução
        """
        agentes = self.inicializar_agentes()
        
        # Definir tasks
        tasks_list = [
            orchestrador_global_task(),
            localizacao_cultural_task(),
            compliance_task(),
            inteligencia_cambial_task(),
            traducao_contextual_task(),
            pesquisa_viral_task(),
            roteiro_short_form_task(),
            copys_social_task(),
            design_visual_task(),
            publicacao_calendario_task(),
            funil_vendas_task(),
            seo_blog_task(),
            nurturing_task(),
            suporte_247_task(),
            analise_sentimento_task()
        ]
        
        crew = Crew(
            name=self.config["nome"],
            agents=list(agentes.values()),
            tasks=tasks_list,
            process=Process.hierarchical,
            manager_agent=agentes["orquestrador"],
            verbose=True
        )
        
        logger.info("Crew criada com sucesso")
        return crew
    
    def executar_campanha(self, campanha: Dict) -> Dict:
        """
        Executa uma campanha completa através da crew.
        
        Args:
            campanha: Dicionário com parâmetros da campanha
            
        Returns:
            Dict: Resultado da execução
        """
        logger.info(f"Executando campanha: {campanha.get('nome', 'Sem nome')}")
        
        crew = self.criar_crew()
        resultado = crew.kickoff(inputs=campanha)
        
        return {
            "status": "completed",
            "campanha": campanha.get("nome"),
            "resultado": resultado,
            "metrics": {
                "agentes_utilizados": len(self.agentes),
                "tasks_executadas": 15
            }
        }


def executar_workflow_campanha_global():
    """
    Workflow principal para execução de campanha global.
    """
    crew_manager = MarketingCrew()
    
    campanha = {
        "nome": "Lançamento Global v2.0",
        "regioes": ["BR", "US", "EU"],
        "objetivos": ["awareness", "conversao"],
        "periodo": "Q1-2026",
        "budget": "R$ 500.000"
    }
    
    resultado = crew_manager.executar_campanha(campanha)
    return resultado


if __name__ == "__main__":
    print("=== Marketing Crew - SaaS Fluxo de Caixa ===")
    
    crew_manager = MarketingCrew()
    agentes = crew_manager.inicializar_agentes()
    
    print(f"\nAgentes carregados:")
    for nome, agente in agentes.items():
        print(f"  - {nome}: {agente.role}")
    
    print("\nConfiguração:")
    print(f"  Mercados: {crew_manager.config['mercados']}")
    print(f"  Idiomas: {crew_manager.config['idiomas']}")
    print(f"  Compliance: {crew_manager.config['compliance_frameworks']}")
