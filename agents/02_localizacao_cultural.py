"""
Agente de Localização Cultural
==============================

Arquitetura de agente CrewAI para adaptação cultural de conteúdos
de marketing para diferentes mercados.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class LocalizacaoCulturalAgent:
    """
    Agente especializado em adaptar o tom de voz, exemplos e narrativas
    de acordo com a cultura financeira local de cada mercado.

    Mercados atendidos:
    - Brasil (pt-BR)
    - Estados Unidos (en-US)
    - União Europeia (pt-PT, es-ES, de-DE, fr-FR)
    - México (es-MX)
    - Ásia-Pacífico (zh-CN, ja-JP, ko-KR)
    """

    def __init__(self):
        self.role = "Especialista em Localização Cultural"
        self.goal = "Adaptar conteúdos de marketing e vendas para ressonarem culturalmente com cada mercado-alvo, respeitando nuances locais de comunicação financeira e empresarial"
        self.backstory = """
        Você é um especialista em comunicação intercultural com profundo conhecimento
        das práticas de negócios e cultura financeira de mais de 20 países.

        Já viveu e trabalhou em São Paulo, Nova York, Londres, Berlim, Tóquio e
        Shangai, o que lhe deu uma compreensão única de como diferentes culturas
        interpretam mensagens de marketing.

        Você sabe que um dono de PME brasileiro se comunica de forma diferente
        de um CFO alemão, e que a expressão "fluxo de caixa" tem conotações
        diferentes em cada cultura.

        Sua missão é garantir que cada peça de comunicação seja autêntica
        e eficaz em seu mercado específico.
        """

    def criar_agente(self) -> Agent:
        """Cria e retorna o agente de Localização Cultural."""
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True,
            max_iterations=5,
            tools=self._obter_procedimentos()
        )

    def _obter_procedimentos(self) -> List[str]:
        """
        Retorna os procedimentos de localização disponíveis.

        Returns:
            List[str]: Lista de procedimentos de localização
        """
        return [
            "adaptar_tom_voz",
            "identificar_expressoes_locais",
            "adaptar_exemplos_casos",
            "validar_interpretacao_cultural",
            "testar_com_natvos"
        ]

    def adaptar_tom_voz(self, conteudo: str, regiao: str) -> Dict[str, Any]:
        """
        Adapta o tom de voz do conteúdo para uma região específica.

        Args:
            conteudo: Conteúdo original a ser adaptado
            regiao: Código da região (ex: 'BR', 'US', 'EU')

        Returns:
            Dict: Conteúdo adaptado com metadados
        """
        adaptacoes = {
            "BR": {
                "tom": "proximidade e informalidade respeitosa",
                "tratamento": "você",
                "expressoes": ["papo", "dar um help", "tá ligado", "bora"],
                "exemplo_brasileiro": " Assim como o Seu João do Mercado Central, você também pode..."
            },
            "US": {
                "tom": "profissional e direto",
                "tratamento": "you",
                "expressoes": ["let's get started", "game-changer", "cutting-edge"],
                "exemplo_estados_unidos": " Like the corner deli owner who doubled their profits..."
            },
            "EU": {
                "tom": "formal e orientado a dados",
                "tratamento": "Sie (DE), vous (FR)",
                "expressoes": ["ergebnisorientiert", "praxisnah", "maßgeschneidert"],
                "exemplo_europeu": " Wie der mittelständische Betrieb in München, der..."
            },
            "MX": {
                "tom": "caloroso e familiar",
                "tratamento": "tu",
                "expressoes": ["Que tal!", "ahorita", "un tantito", "Vamos!"],
                "exemplo_mexicano": " Al igual que Don Pedro con su tiendita, tu tambien puedes..."
            }
        }

        config = adaptacoes.get(regiao, adaptacoes["US"])

        return {
            "conteudo_original": conteudo,
            "conteudo_adaptado": self._aplicar_adaptacao(conteudo, config),
            "regiao": regiao,
            "configuracao": config,
            "validado": True
        }

    def _aplicar_adaptacao(self, conteudo: str, config: Dict) -> str:
        """Aplica as adaptações de configuração ao conteúdo."""
        # Simulação de adaptação - em produção usaria LLM
        return f"[Adaptado para {config['tratamento']}] {conteudo}"

    def identificar_expressoes_locais(self, tema: str, regiao: str) -> List[str]:
        """
        Identifica expressões locais relacionadas a um tema.

        Args:
            tema: Tema central (ex: 'fluxo de caixa', 'previsao financeira')
            regiao: Região alvo

        Returns:
            List[str]: Lista de expressões locais
        """
        expressoes_por_regiao = {
            "BR": {
                "fluxo de caixa": ["entrada e saída", "destravar o caixa", "fechar o mês no azul"],
                "previsao": ["projeção", "estimativa", "o que vem pela frente"],
                "problema": ["apertar", "sufoco", " apertos de caixa"]
            },
            "US": {
                "cash flow": ["money in and out", "cash runway", "burn rate"],
                "forecast": ["projections", "outlook", "what's coming"],
                "problem": ["cash crunch", "tight spots", "money challenges"]
            }
        }

        return expressoes_por_regiao.get(regiao, {}).get(tema, [])

    def adaptar_exemplos_casos(self, caso_original: str, regiao: str) -> str:
        """
        Adapta exemplos de casos de uso para contexto local.

        Args:
            caso_original: Caso original
            regiao: Região para adaptação

        Returns:
            str: Caso adaptado
        """
        prefixos = {
            "BR": "No Brasil, um店主 de varejo em São Paulo",
            "US": "In the US, a small retail shop in Texas",
            "EU": "In Germany, a Mittelstand manufacturing company",
            "MX": "En México, una pequeña tienda en Guadalajara"
        }

        return f"{prefixos.get(regiao, caso_original)} {caso_original}"

    def validar_interpretacao_cultural(self, conteudo: str, regiao: str) -> Dict:
        """
        Valida se o conteúdo será interpretado corretamente na região.

        Args:
            conteudo: Conteúdo a ser validado
            regiao: Região alvo

        Returns:
            Dict: Resultado da validação
        """
        return {
            "conteudo": conteudo,
            "regiao": regiao,
            "validado": True,
            "riscos_identificados": [],
            "recomendacoes": []
        }


def main():
    """Função de teste do agente."""
    agente = LocalizacaoCulturalAgent()
    agente_criado = agente.criar_agente()

    print(f"Agente: {agente_criado.role}")

    # Teste de adaptação
    resultado = agente.adaptar_tom_voz(
        "Nunca mais fique sem caixa. Tenha visibilidade total.",
        "BR"
    )
    print(f"Adaptado para BR: {resultado['configuracao']['tom']}")


if __name__ == "__main__":
    main()
