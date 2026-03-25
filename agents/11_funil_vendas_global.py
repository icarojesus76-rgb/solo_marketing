"""
Agente de Funil de Vendas Global
=================================

Arquitetura de agente CrewAI para mapear e desenhar o funil de vendas
completo por região com canais, automações e scripts.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class FunilVendasGlobalAgent:
    """
    Agente especializado em mapear e otimizar funis de vendas B2B
    para diferentes regiões e segmentos de mercado.
    """

    def __init__(self):
        self.role = "Arquiteto de Funil de Vendas Global"
        self.goal = "Desenhar e otimizar funis de vendas que maximizam conversão de leads em clientes pagantes em múltiplos mercados"
        self.backstory = """
        Você é um arquiteto de vendas com 15 anos de experiência construindo
        funis de vendas para empresas de SaaS B2B em escala global.
        
        Você já construiu funis que geraram mais de R$ 100 milhões em receita
        e entende que cada mercado tem suas particularidades.
        
        Sua especialidade:
        - Funis de entrada dupla (PLG + Sales-assist)
        - Automação de nutrição multilíngue
        - Scoring de leads por região
        - Operações de vendas em múltiplos fusos
        """

    def criar_agente(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True
        )

    def mapear_funil(
        self,
        regiao: str,
        tipo_negocio: str = "saas_b2b"
    ) -> Dict[str, Any]:
        """
        Mapeia funil de vendas completo para região.

        Args:
            regiao: Região do mercado
            tipo_negocio: Tipo de negócio

        Returns:
            Dict: Funil completo mapeado
        """
        etapas = [
            {"estagio": "TOFU", "nome": "Awareness",
                "descricao": "Geração de visibilidade"},
            {"estagio": "MOFU", "nome": "Consideração",
                "descricao": "Lead se informa"},
            {"estagio": "BOFU", "nome": "Decisão",
                "descricao": "Avaliação e compra"},
            {"estagio": "POS-VENDA", "nome": "Onboarding",
                "descricao": "Ativação e sucesso"},
            {"estagio": "EXPANSÃO", "nome": "Upsell", "descricao": "Crescimento"}
        ]

        return {
            "id": f"FUNIL-{regiao}",
            "regiao": regiao,
            "tipo": tipo_negocio,
            "estagios": etapas,
            "canais_entrada": self._obter_canais_entrada(regiao),
            "automacoes": self._obter_automacoes(regiao),
            "scripts": self._obter_scripts(regiao),
            "kpis_por_estagio": self._obter_kpis()
        }

    def _obter_canais_entrada(self, regiao: str) -> List[Dict]:
        """Retorna canais de entrada por região."""
        canais = {
            "BR": [
                {"canal": "Google Ads", "peso": 0.3, "cpl_medio": 80},
                {"canal": "Meta Ads", "peso": 0.25, "cpl_medio": 60},
                {"canal": "Orgânico (SEO)", "peso": 0.2, "cpl_medio": 0},
                {"canal": "Indicações", "peso": 0.15, "cpl_medio": 100},
                {"canal": "Parceiros", "peso": 0.1, "cpl_medio": 50}
            ],
            "US": [
                {"canal": "LinkedIn Ads", "peso": 0.35, "cpl_medio": 150},
                {"canal": "Google Ads", "peso": 0.3, "cpl_medio": 120},
                {"canal": "Outbound", "peso": 0.2, "cpl_medio": 200},
                {"canal": "Orgânico", "peso": 0.15, "cpl_medio": 0}
            ]
        }
        return canais.get(regiao, canais["BR"])

    def _obter_automacoes(self, regiao: str) -> List[Dict]:
        """Retorna automações do funil."""
        return [
            {
                "nome": "Lead Scoring",
                "gatilho": "Form submission",
                "acao": "Score baseado em: cargo, empresa, interação"
            },
            {
                "nome": "Nurturing Sequence",
                "gatilho": "Score < threshold",
                "acao": "E-mail + WhatsApp automatizados"
            },
            {
                "nome": "SDR Alert",
                "gatilho": "Score > threshold",
                "acao": "Notificar SDR via Slack"
            },
            {
                "nome": "Trial Start",
                "gatilho": "Trial initiated",
                "acao": "Onboarding + Sequencia D+1, D+3, D+7"
            }
        ]

    def _obter_scripts(self, regiao: str) -> List[Dict]:
        """Retorna scripts de vendas."""
        return [
            {
                "momento": "Primeiro contato",
                "idioma": "pt-BR" if regiao == "BR" else "en-US",
                "template": "Olá {nome}, vi que você se inscreveu no [PRODUTO]..."
            },
            {
                "momento": "Discovery",
                "perguntas": [
                    "Como você gerencia fluxo de caixa hoje?",
                    "Quais os maiores desafios?",
                    "Quem mais está envolvido na decisão?"
                ]
            },
            {
                "momento": "Demo",
                "foco": "ROI, tempo de setup, integração"
            }
        ]

    def _obter_kpis(self) -> Dict:
        """Retorna KPIs por estágio."""
        return {
            "awareness": {"visitas": 10000, "taxa_conversao": 0.02},
            "consideracao": {"leads": 200, "taxa_conversao": 0.15},
            "decisao": {"mqls": 30, "taxa_conversao": 0.25},
            "venda": {"clientes": 7.5, "ticket_medio": 1500},
            " retenção": {"churn": 0.03, "nps": 45}
        }

    def calcular_unit_economics(self, funil: Dict) -> Dict:
        """Calcula unit economics do funil."""
        kpis = funil["kpis_por_estagio"]

        cac = 100  # Exemplo
        ltv = kpis["venda"]["ticket_medio"] / kpis[" retenção"]["churn"]

        return {
            "cac": cac,
            "ltv": ltv,
            "ltv_cac_ratio": ltv / cac,
            "payback_meses": 12,
            "margem_contribuicao": 0.7
        }


def main():
    agente = FunilVendasGlobalAgent()
    funil = agente.mapear_funil("BR")
    print(f"Funil: {funil['id']}")
    print(f"Estágios: {len(funil['estagios'])}")
    print(f"Canais: {len(funil['canais_entrada'])}")


if __name__ == "__main__":
    main()
