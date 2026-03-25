"""
Agente de Tradução Contextual
=============================

Arquitetura de agente CrewAI para tradução de conteúdos financeiros
complexos com precisão técnica e fluidez em múltiplos idiomas.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class TraducaoContextualAgent:
    """
    Agente especializado em traduzir conteúdos financeiros complexos
    com precisão técnica e fluidez em múltiplos idiomas.

    Idiomas suportados:
    - Português (Brasil e Portugal)
    - Inglês (EUA e UK)
    - Espanhol (Espanha, México, América Latina)
    - Alemão
    - Francês
    - Chinês (Simplificado)
    - Japonês
    """

    def __init__(self):
        self.role = "Especialista em Tradução Contextual Financeira"
        self.goal = "Traduzir conteúdos financeiros e de marketing com precisão técnica, mantendo o impacto persuasivo e clareza em múltiplos idiomas"
        self.backstory = """
        Você é um tradutor especializado com 15 anos de experiência em 
        tradução de conteúdos financeiros e de tecnologia para empresas B2B.
        
        Nativo em português brasileiro, você também domina fluentemente 
        inglês americano, espanhol (multiple dialectos), alemão e francês.
        
        Sua especialidade é a tradução de conceitos financeiros complexos 
        de forma que ressoe com o público local. Você entende que:
        - "Cash flow" em inglês não é simplesmente "fluxo de caixa" em português
        - CFOs alemães usam termos diferentes de CFOs americanos
        - A cultura de negócios japonesa requer uma abordagem completamente 
          diferente de comunicação
        
        Você não apenas traduz palavras, você traduz significado, tom e 
        impacto persuasivo para cada contexto cultural.
        """

    def criar_agente(self) -> Agent:
        """Cria e retorna o agente de Tradução Contextual."""
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True,
            max_iterations=5
        )

    def traduzir_conteudo(
        self,
        conteudo: str,
        idioma_origem: str,
        idioma_destino: str,
        tipo_conteudo: str = "marketing"
    ) -> Dict[str, Any]:
        """
        Traduz conteúdo mantendo contexto e impacto.

        Args:
            conteudo: Conteúdo original
            idioma_origem: Código do idioma de origem (ex: 'pt-BR')
            idioma_destino: Código do idioma de destino (ex: 'en-US')
            tipo_conteudo: Tipo do conteúdo (marketing, técnico, legal)

        Returns:
            Dict: Resultado da tradução com metadados
        """
        traducoes = {
            ("pt-BR", "en-US"): {
                "fluxo de caixa": "cash flow management",
                "apertos de caixa": "cash crunch",
                "previsão": "forecast",
                "visibilidade": "real-time visibility",
                " Nunca mais fique sem caixa": "Never run out of cash again",
                "tenha visibilidade total": "gain complete visibility"
            },
            ("pt-BR", "es-ES"): {
                "fluxo de caja": "flujo de caja",
                "apertos de caja": "presiones de efectivo",
                "previsão": "pronóstico",
                "visibilidade": "visibilidad total",
                " Nunca mais fique sem caixa": "Nunca más te quedes sin efectivo",
                "tenha visibilidade total": "obtén visibilidad completa"
            },
            ("pt-BR", "de-DE"): {
                "fluxo de caixa": "Liquiditätsmanagement",
                "apertos de caixa": "Liquiditätsengpässe",
                "previsão": "Prognose",
                "visibilidade": "Echtzeit-Transparenz",
                " Nunca mais fique sem caixa": "Nie wieder ohne Liquidität dastehen",
                "tenha visibilidade total": "erhalten Sie vollständige Transparenz"
            }
        }

        # Simulação de tradução
        traducao = conteudo
        if (idioma_origem, idioma_destino) in traducoes:
            for original, traduzido in traducoes[(idioma_origem, idioma_destino)].items():
                traducao = traducao.replace(original, traduzido)

        return {
            "conteudo_original": conteudo,
            "traducao": traducao,
            "idioma_origem": idioma_origem,
            "idioma_destino": idioma_destino,
            "tipo_conteudo": tipo_conteudo,
            "qualidade_estimada": "Alta",
            "revisoes_requeridas": 0,
            "adaptações_culturais": self._identificar_adaptacoes(
                conteudo, idioma_destino
            )
        }

    def _identificar_adaptacoes(self, conteudo: str, idioma_destino: str) -> List[str]:
        """Identifica adaptações culturais necessárias."""
        adaptacoes = []

        if idioma_destino == "de-DE":
            adaptacoes.append("Tom mais formal e direto")
            adaptacoes.append("Ênfase em dados e precisão")

        if idioma_destino == "en-US":
            adaptacoes.append("Linguagem action-oriented")
            adaptacoes.append("CTAs mais diretos")

        if idioma_destino == "ja-JP":
            adaptacoes.append("Tom muito formal")
            adaptacoes.append("Evitar linguagem muito direta")
            adaptacoes.append("Considerar KEIGO (linguagem honorífica)")

        return adaptacoes

    def traduzir_termo_tecnico(
        self,
        termo: str,
        idioma_origem: str,
        idioma_destino: str
    ) -> Dict[str, str]:
        """
        Traduz termo técnico mantendo precisão.

        Args:
            termo: Termo técnico a traduzir
            idioma_origem: Idioma de origem
            idioma_destino: Idioma de destino

        Returns:
            Dict: Tradução do termo
        """
        dicionario_tecnico = {
            "fluxo de caixa operacional": {
                "en-US": "Operating cash flow",
                "de-DE": "Operativer Cashflow",
                "es-ES": "Flujo de caja operativo",
                "fr-FR": "Flux de trésorerie d'exploitation"
            },
            "demonstrativo de fluxo de caixa": {
                "en-US": "Cash flow statement",
                "de-DE": "Kapitalflussrechnung",
                "es-ES": "Estado de flujos de efectivo",
                "fr-FR": "Tableau des flux de trésorerie"
            },
            "conciliação bancária": {
                "en-US": "Bank reconciliation",
                "de-DE": "Bankabstimmung",
                "es-ES": "Conciliación bancaria",
                "fr-FR": "Réconciliation bancaire"
            }
        }

        termo_lower = termo.lower()
        traducao = dicionario_tecnico.get(
            termo_lower, {}).get(idioma_destino, termo)

        return {
            "termo_original": termo,
            "termo_traduzido": traducao,
            "idioma_destino": idioma_destino,
            "encontrado": termo_lower in dicionario_tecnico
        }

    def adaptar_microcopy(
        self,
        microcopy: str,
        idioma_destino: str
    ) -> Dict[str, Any]:
        """
        Adapta microcopy (botões, labels, mensagens de erro) para diferentes idiomas.

        Args:
            microcopy: Microcopy original
            idioma_destino: Idioma de destino

        Returns:
            Dict: Microcopy adaptado
        """
        adaptacoes_microcopy = {
            "pt-BR": {
                "Criar conta": "Criar conta",
                "Começar grátis": "Começar grátis",
                "Fale conosco": "Fale conosco"
            },
            "en-US": {
                "Criar conta": "Create account",
                "Começar grátis": "Start free",
                "Fale conosco": "Contact us"
            },
            "de-DE": {
                "Criar conta": "Konto erstellen",
                "Começar grátis": "Kostenlos starten",
                "Fale conosco": "Kontaktieren Sie uns"
            }
        }

        # Simulação de adaptação
        adaptado = adaptacoes_microcopy.get(idioma_destino, {}).get(
            microcopy,
            f"[{idioma_destino}] {microcopy}"
        )

        return {
            "original": microcopy,
            "adaptado": adaptado,
            "idioma": idioma_destino,
            "consideracoes": [
                "Verificar limites de caracteres",
                "Testar com nativos",
                "Ajustar para mobile se necessário"
            ]
        }


def main():
    """Função de teste do agente."""
    agente = TraducaoContextualAgent()

    print("=== Tradução Português -> Inglês ===")
    resultado = agente.traduzir_conteudo(
        "Nunca mais fique sem caixa. Tenha visibilidade total.",
        "pt-BR",
        "en-US"
    )
    print(f"Original: {resultado['conteudo_original']}")
    print(f"Tradução: {resultado['traducao']}")

    print("\n=== Adaptação de Microcopy ===")
    micro = agente.adaptar_microcopy("Começar grátis", "de-DE")
    print(f"Alemanha: {micro['adaptado']}")


if __name__ == "__main__":
    main()
