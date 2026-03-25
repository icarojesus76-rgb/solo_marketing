"""
Agente de Inteligência Cambial e Preço
======================================

Arquitetura de agente CrewAI para definição de estratégias de precificação
ajustadas ao poder de compra, câmbio e concorrência de cada mercado.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class InteligenciaCambialPrecoAgent:
    """
    Agente especializado em definir planos de assinatura ajustados ao poder
    de compra, câmbio e concorrência de cada mercado global.

    Responsabilidades:
    - Monitorar taxas de câmbio em tempo real
    - Analisar poder de compra por região
    - Definir estratégias de preços localizedas
    - Competir com soluções locais
    - Otimizar revenue por mercado
    """

    def __init__(self):
        self.role = "Especialista em Inteligência Cambial e Estratégia de Preços"
        self.goal = "Definir e otimizar estratégias de precificação que maximizem revenue mantendo competitividade e acessibilidade em cada mercado global"
        self.backstory = """
        Você é um especialista em pricing internacional com 20 anos de experiência 
        em empresas de SaaS globais. Formado em Economia pela FGV com MBA em 
        Estratégia pela Harvard Business School.
        
        Já estruturou estratégias de preços para launches em mais de 40 países, 
        sempre equilibrando rentabilidade com acessibilidade local.
        
        Você entende que o poder de compra de um CFO brasileiro é diferente 
        de um CFO alemão, e que estratégias de preço devem considerar:
        - Paridade de poder de compra (PPP)
        - Taxas de câmbio e volatilidade
        - Concorrência local e global
        - Sensibilidade a preço do mercado
        - Custos de serviço local
        
        Sua missão é encontrar o ponto ideal onde maximizamos revenue 
        sem sacrificar a penetração de mercado.
        """

    def criar_agente(self) -> Agent:
        """Cria e retorna o agente de Inteligência Cambial e Preço."""
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True,
            max_iterations=5
        )

    def obter_cotacoes(self) -> Dict[str, float]:
        """
        Obtém taxas de câmbio atuais para mercados-alvo.

        Returns:
            Dict: Taxas de câmbio vs BRL (moeda base)
        """
        # Em produção, integraria com API de câmbio (ex: Open Exchange Rates)
        cotacoes = {
            "BRL": 1.0,       # Moeda base
            "USD": 5.05,      # Dólar americano
            "EUR": 5.50,      # Euro
            "GBP": 6.40,      # Libra esterlina
            "MXN": 0.29,      # Peso mexicano
            "ARS": 0.005,     # Peso argentino
            "CLP": 0.0055,    # Peso chileno
            "COP": 0.0013,    # Peso colombiano
            "JPY": 0.034,     # Iene japonês
            "CNY": 0.70       # Yuan chinês
        }

        logger.info(f"Obtidas {len(cotacoes)} cotações de câmbio")
        return cotacoes

    def analisar_poder_compra(self, regiao: str) -> Dict[str, Any]:
        """
        Analisa o poder de compra médio na região para PMEs.

        Args:
            regiao: Código da região (ex: 'BR', 'US', 'EU')

        Returns:
            Dict: Análise de poder de compra
        """
        analises = {
            "BR": {
                "pib_per_capita_usd": 8917,
                "faturamento_medio_pme_brl": 2500000,
                "faturamento_medio_pme_usd": 495,
                "orcamento_tecnologia_percentual": 0.03,
                "preco_servico_premium_brl": 500,
                "preco_servico_premium_usd": 99,
                "sensibilidade_preco": "Alta",
                "concorrentes_locais": [" ContaAzul", "Contabilizei", "QuickBooks"]
            },
            "US": {
                "pib_per_capita_usd": 63530,
                "faturamento_medio_pme_usd": 500000,
                "orcamento_tecnologia_percentual": 0.05,
                "preco_servico_premium_usd": 299,
                "sensibilidade_preco": "Média",
                "concorrentes_locais": ["QuickBooks", "Xero", "FreshBooks", "Wave"]
            },
            "EU": {
                "pib_per_capita_usd": 35000,
                "faturamento_medio_pme_eur": 450000,
                "orcamento_tecnologia_percentual": 0.04,
                "preco_servico_premium_eur": 149,
                "sensibilidade_preco": "Média-Alta",
                "concorrentes_locais": ["DATEV", "Sage", "Exact", "Tripletex"]
            }
        }

        return analises.get(regiao, analises["BR"])

    def definir_estrutura_precos(self, regiao: str) -> Dict[str, Any]:
        """
        Define a estrutura de preços completa para uma região.

        Args:
            regiao: Código da região

        Returns:
            Dict: Estrutura de preços definida
        """
        cotacoes = self.obter_cotacoes()
        poder_compra = self.analisar_poder_compra(regiao)

        # Cálculo de preços ajustados por região
        # Preço base em USD é $29/mês
        preco_base_usd = 29

        if regiao == "BR":
            # Paridade de poder de compra Brasil: ~10x mais barato
            fator_ppp = 0.10
            moedas = ["BRL"]
        elif regiao == "US":
            fator_ppp = 1.0
            moedas = ["USD"]
        elif regiao == "EU":
            # Europa ~0.6x do preço US
            fator_ppp = 0.85
            moedas = ["EUR", "GBP"]
        else:
            fator_ppp = 0.70
            moedas = ["USD"]

        planos = {
            "starter": {
                "nome": "Starter",
                "precos": {},
                "funcionalidades": [
                    "Até 500 transações/mês",
                    "3 usuários",
                    "Relatórios básicos",
                    "Integração bancária básica"
                ]
            },
            "professional": {
                "nome": "Professional",
                "precos": {},
                "funcionalidades": [
                    "Transações ilimitadas",
                    "10 usuários",
                    "Previsão de caixa com IA",
                    "Integrações completas",
                    "API access"
                ]
            },
            "enterprise": {
                "nome": "Enterprise",
                "precos": {},
                "funcionalidades": [
                    "Tudo do Professional",
                    "Usuários ilimitados",
                    "White-label",
                    "Account manager dedicado",
                    "SLA 99.9%"
                ]
            }
        }

        # Definir preços por moeda
        precos_base = {
            "starter": 0.35,      # USD
            "professional": 0.70,  # USD
            "enterprise": 1.5     # USD
        }

        for plano, preco in precos_base.items():
            for moeda in moedas:
                if moeda == "BRL":
                    planos[plano]["precos"][moeda] = f"R$ {int(preco * 100 * fator_ppp)}"
                elif moeda == "USD":
                    planos[plano]["precos"][moeda] = f"${preco * fator_ppp:.2f}"
                elif moeda == "EUR":
                    planos[plano]["precos"][moeda] = f"€{preco * fator_ppp:.2f}"

        return {
            "regiao": regiao,
            "poder_compra": poder_compra,
            "planos": planos,
            "currency_multiplier": fator_ppp,
            "paridade_recomendada": f"{1/fator_ppp:.1f}x vs preço US",
            "data_atualizacao": "2026-03-25"
        }

    def analisar_concorrencia(self, regiao: str) -> List[Dict]:
        """
        Analisa estratégias de preço dos concorrentes.

        Args:
            regiao: Região para análise

        Returns:
            List: Análise dos concorrentes
        """
        analises_concorrentes = {
            "BR": [
                {"nome": "ContaAzul", "plano_base": "R$ 37/mês",
                    "funcionalidades": "similar"},
                {"nome": "Contabilizei", "plano_base": "R$ 89/mês",
                    "funcionalidades": "contador incluso"},
                {"nome": "QuickBooks", "plano_base": "R$ 79/mês",
                    "funcionalidades": "similar"}
            ],
            "US": [
                {"nome": "QuickBooks Simple Start",
                    "plano_base": "$25/mês", "funcionalidades": "básico"},
                {"nome": "Wave", "plano_base": "Grátis + $25/transação",
                    "funcionalidades": "freemium"},
                {"nome": "FreshBooks", "plano_base": "$17/mês",
                    "funcionalidades": "similar"}
            ]
        }

        return analises_concorrentes.get(regiao, [])

    def gerar_recomendacao_preco(
        self,
        regiao: str,
        estrategia: str = "penetracao"
    ) -> Dict[str, Any]:
        """
        Gera recomendação de preço otimizada.

        Args:
            regiao: Região alvo
            estrategia: Estratégia de pricing (penetracao, premium, competitivo)

        Returns:
            Dict: Recomendação de preço detalhada
        """
        estrutura = self.definir_estrutura_precos(regiao)
        concorrencia = self.analisar_concorrencia(regiao)

        recomendacoes = {
            "penetracao": {
                "objetivo": "Ganhar market share rapidamente",
                "desconto_inicial": "30% no primeiro ano",
                "meta_conversao": "+50% vs preço cheio"
            },
            "premium": {
                "objetivo": "Posicionar como solução de alta qualidade",
                "diferencial": "Funcionalidades exclusivas",
                "meta_perfil": "PMEs maiores e mais sofisticadas"
            },
            "competitivo": {
                "objetivo": "Competir diretamente com concorrentes",
                "preco_referencia": "10% abaixo do principal concorrente",
                "meta": "Equalizar valor percebido"
            }
        }

        return {
            "regiao": regiao,
            "estrategia": estrategia,
            "recomendacao": recomendacoes.get(estrategia, recomendacoes["competitivo"]),
            "estrutura_precos": estrutura,
            "analise_concorrencia": concorrencia,
            "proximo_passos": [
                "Aprovar estrutura com time de produto",
                "Implementar gateway de pagamento localizedo",
                "Configurar conversão de moedas",
                "Testar com oferta de lançamento"
            ]
        }


def main():
    """Função de teste do agente."""
    agente = InteligenciaCambialPrecoAgent()

    print("=== Análise de Preços Brasil ===")
    resultado_br = agente.definir_estrutura_precos("BR")
    print(f"Estratégia BR: {resultado_br['paridade_recomendada']}")
    print(f"Planos: {list(resultado_br['planos'].keys())}")

    print("\n=== Recomendação para EUA ===")
    rec_us = agente.gerar_recomendacao_preco("US", "premium")
    print(f"Estratégia: {rec_us['recomendacao']['objetivo']}")


if __name__ == "__main__":
    main()
