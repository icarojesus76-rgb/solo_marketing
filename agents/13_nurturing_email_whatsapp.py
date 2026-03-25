"""
Agente de Nurturing (E-mail + WhatsApp)
========================================

Arquitetura de agente CrewAI para desenhar sequências de nutrição
de leads para conversão em trial, demo ou assinatura.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class NurturingEmailWhatsappAgent:
    """
    Agente especializado em criar sequências de nutrição automatizadas
    para e-mail e WhatsApp que convertem leads frios em clientes.
    """

    def __init__(self):
        self.role = "Especialista em Nurturing e Automação"
        self.goal = "Criar sequências de nutrição que educam, engajam e convertem leads através de múltiplos canais"
        self.backstory = """
        Você é um especialista em marketing de relacionamento com 12 anos 
        de experiência criando sequências de nurturing que convertem.
        
        Você entende que:
        - Cada lead é único e deve ser tratado assim
        - Sequências devem adicionar valor genuíno
        - Timing é crucial
        - Multi-channel é mais eficaz
        """

    def criar_agente(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True
        )

    def gerar_sequencia_nurturing(
        self,
        objetivo: str,
        canal: str,
        idioma: str
    ) -> Dict[str, Any]:
        """
        Gera sequência completa de nurturing.

        Args:
            objetivo: Objetivo (trial, demo, assinatura)
            canal: Canal (email, whatsapp)
            idioma: Idioma

        Returns:
            Dict: Sequência completa
        """
        sequencias = {
            ("trial", "email", "pt-BR"): [
                {"dia": 1,
                    "assunto": "Bem-vindo ao [PRODUTO]!", "tempo": "10h"},
                {"dia": 3, "assunto": "Seu primeiro passo para controlar o caixa",
                    "tempo": "10h"},
                {"dia": 5, "assunto": "Como PMEs economizam R$ 5.000/mês", "tempo": "10h"},
                {"dia": 7, "assunto": "Último dia de trial - não perca!", "tempo": "10h"}
            ],
            ("whatsapp", "pt-BR"): [
                {"dia": 1, "mensagem": "Olá! Bem-vindo! Como posso ajudar?"},
                {"dia": 3, "mensagem": "Já conheceu nosso tutorial de fluxo de caixa?"},
                {"dia": 7, "mensagem": "Posso agendar uma demo personalizada?"}
            ]
        }

        key = (canal, idioma) if objetivo == "trial" else (canal, idioma)
        emails = sequencias.get(key, sequencias.get((canal, idioma), []))

        return {
            "id": f"NURT-{objetivo.upper()}-{canal.upper()}-{idioma}",
            "objetivo": objetivo,
            "canal": canal,
            "idioma": idioma,
            "emails": emails,
            "total_envios": len(emails),
            "duracao_dias": emails[-1]["dia"] if emails else 0
        }

    def gerar_email_marketing(
        self,
        tipo: str,
        idioma: str
    ) -> Dict[str, Any]:
        """Gera template de e-mail marketing."""
        templates = {
            ("welcome", "pt-BR"): {
                "assunto": "Bem-vindo ao [PRODUTO]! 🚀",
                "preheader": "Seu primeiro passo para controlar o caixa",
                "corpo": """
Olá {nome},

Seja bem-vindo ao [PRODUTO]!

Você está a um passo de transformar a gestão financeira da sua empresa.

O que fazer agora:
1. Acesse sua conta
2. Conecte seu banco
3. Veja seu fluxo de caixa

Qualquer dúvida, responda este e-mail!

Abraços,
Time [PRODUTO]
                """.strip()
            },
            ("content", "pt-BR"): {
                "assunto": "{conteudo_titulo} - Dica {numero}",
                "preheader": "Veja como melhorar seu caixa",
                "corpo": """
Olá {nome},

Você sabia que [insight_interessante]?

[conteudo_valioso]

Quer aprender mais? Assista ao tutorial completo.

[CTA: Acessar agora]

Abraços,
Time [PRODUTO]
                """.strip()
            }
        }

        return templates.get((tipo, idioma), templates.get(("welcome", "pt-BR")))

    def gerar_whatsapp_template(
        self,
        tipo: str,
        idioma: str
    ) -> Dict[str, Any]:
        """Gera template de WhatsApp."""
        templates = {
            ("welcome", "pt-BR"): {
                "mensagem": """
Olá {nome}! 👋

Seja bem-vindo(a) ao [PRODUTO]!

Estou aqui para te ajudar no que precisar. 

Já conheceu nossa demo? É rapidinho!

👉 [LINK_DEMO]

Qualquer dúvida, é só perguntar! 😊
                """.strip()
            },
            ("follow_up", "pt-BR"): {
                "mensagem": """
Oi {nome}!

Vi que você começou a usar o [PRODUTO]. Como está sendo sua experiência?

Precisa de ajuda com algo?

Estamos aqui para você! 💪
                """.strip()
            }
        }

        return templates.get((tipo, idioma), templates.get(("welcome", "pt-BR")))


def main():
    agente = NurturingEmailWhatsappAgent()
    seq = agente.gerar_sequencia_nurturing("trial", "email", "pt-BR")
    print(f"Sequência: {seq['id']}")
    print(f"Total emails: {seq['total_envios']}")


if __name__ == "__main__":
    main()
