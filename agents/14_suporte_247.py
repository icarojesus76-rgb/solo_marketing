"""
Agente de Suporte 24/7
=======================

Arquitetura de agente CrewAI para responder dúvidas sobre fluxo de caixa,
onboarding e uso do produto em múltiplos idiomas.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class Suporte247Agent:
    """
    Agente especializado em fornecer suporte ao cliente 24/7
    em múltiplos idiomas para dúvidas sobre produto e fluxo de caixa.
    """

    def __init__(self):
        self.role = "Agente de Suporte ao Cliente 24/7"
        self.goal = "Resolver dúvidas de clientes de forma rápida, eficiente e amigável, 24 horas por dia, 7 dias por semana"
        self.backstory = """
        Você é um agente de suporte ao cliente com conhecimento profundo
        do produto e do nicho de gestão financeira para PMEs.
        
        Você é:
        - Paciente e empático
        - Extremamente knowledgeable
        - Focado em resolver na primeira interação
        - Multilíngue
        """

    def criar_agente(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True
        )

    def responder_duvida(
        self,
        pergunta: str,
        idioma: str,
        contexto: Dict = None
    ) -> Dict[str, Any]:
        """
        Responde dúvida do cliente.

        Args:
            pergunta: Pergunta do cliente
            idioma: Idioma de preferência
            contexto: Contexto adicional

        Returns:
            Dict: Resposta com metadados
        """
        # Base de conhecimento simplificada
        kb = {
            "pt-BR": {
                "como conectar banco": "Vá em Configurações > Integrações > Banco...",
                "como fazer previsao": "Acesse a aba Previsão e configure...",
                "onboarding": "O onboarding tem 5 passos..."
            },
            "en-US": {
                "how to connect bank": "Go to Settings > Integrations > Bank...",
                "how to forecast": "Access the Forecast tab and configure...",
                "onboarding": "Onboarding has 5 steps..."
            }
        }

        resposta = self._buscar_resposta(pergunta, idioma, kb)

        return {
            "id": f"TICKET-{pergunta[:10].upper()}",
            "pergunta": pergunta,
            "idioma": idioma,
            "resposta": resposta,
            "resolved": True,
            "tempo_resposta_segundos": 5,
            "escalation_needed": False,
            "artigos_relacionados": [
                "Guia de integração bancária",
                "Tutorial de previsão"
            ]
        }

    def _buscar_resposta(self, pergunta: str, idioma: str, kb: Dict) -> str:
        """Busca resposta na base de conhecimento."""
        kb_idioma = kb.get(idioma, kb.get("pt-BR", {}))

        pergunta_lower = pergunta.lower()

        for key, value in kb_idioma.items():
            if key in pergunta_lower:
                return value

        return f"Obrigado pela pergunta! Vou verificar isso para você. Por favor, aguarde um momento."

    def gerar_kb_artigo(
        self,
        topico: str,
        idioma: str
    ) -> Dict[str, Any]:
        """Gera artigo para base de conhecimento."""
        return {
            "id": f"KB-{topico[:10].upper()}-{idioma}",
            "topico": topico,
            "idioma": idioma,
            "titulo": self._gerar_titulo(topico, idioma),
            "categorias": ["Produto", "Finanças", "Técnico"],
            "tags": ["fluxo de caixa", "tutorial", topico],
            "conteudo": {
                "resumo": f"Como fazer {topico} no [PRODUTO]",
                "passos": [
                    "Passo 1: Acesse...",
                    "Passo 2: Configure...",
                    "Passo 3: Visualize..."
                ],
                "faq": [
                    "Posso fazer X?",
                    "Quanto tempo leva?"
                ]
            }
        }

    def _gerar_titulo(self, topico: str, idioma: str) -> str:
        """Gera título do artigo."""
        if idioma == "pt-BR":
            return f"Como fazer {topico} - Guia Completo"
        elif idioma == "en-US":
            return f"How to {topico} - Complete Guide"
        return f"{topico} Guide"


def main():
    agente = Suporte247Agent()
    resp = agente.responder_duvida("Como conectar meu banco?", "pt-BR")
    print(f"Ticket: {resp['id']}")
    print(f"Resposta: {resp['resposta'][:50]}...")


if __name__ == "__main__":
    main()
