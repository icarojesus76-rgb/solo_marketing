"""
Agente de Roteiro para Short-Form
=================================

Arquitetura de agente CrewAI para criar roteiros de 10-60 segundos
para Reels, TikTok e Shorts explicando fluxo de caixa de forma simples.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class RoteiroShortFormAgent:
    """
    Agente especializado em criar roteiros para conteúdo de short-form video
    com estrutura otimizada para engajamento e conversão.
    """

    def __init__(self):
        self.role = "Roteirista de Short-Form Content"
        self.goal = "Criar roteiros viciantes de 10-60 segundos que eduquem sobre fluxo de caixa enquanto maximizam engajamento e conversões"
        self.backstory = """
        Você é um roteirista especialista em conteúdo de curta duração com 
        8 anos de experiência criando vídeos virais para marcas B2B e B2C.
        
        Você conhece a anatomia perfeita de um vídeo viral:
        - Hook nos primeiros 2 segundos
        - Problema que gera identificação
        - Solução clara e valiosa
        - CTA irresistível
        
        No nicho de finanças, você sabe que o equilíbrio entre 
        educacional e entretenível é a chave para viralização.
        """

    def criar_agente(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True
        )

    def gerar_roteiro(
        self,
        tema: str,
        duracao: int = 30,
        plataforma: str = "tiktok"
    ) -> Dict[str, Any]:
        """
        Gera roteiro completo para video short-form.

        Args:
            tema: Tema do vídeo
            duracao: Duração em segundos (10-60)
            plataforma: Plataforma alvo

        Returns:
            Dict: Roteiro completo com estrutura
        """
        template = self._obter_template(plataforma)

        ganchos = [
            "Você sabia que 73% dos donos de PME não sabem quanto têm no banco?",
            "POV: Seu contador te mostra o fluxo de caixa pela primeira vez",
            "O momento em que você para de usar planilha...",
            "3 sinais de que sua empresa vai ter problemas de caixa"
        ]

        return {
            "id": f"ROT-{tema[:10].upper()}-001",
            "tema": tema,
            "duracao": duracao,
            "plataforma": plataforma,
            "gancho": ganchos[0],
            "estrutura": {
                "0-3s": "GANCHO - Frase de impacto que gera curiosidade",
                "3-10s": "CONTEXTO - Explicação rápida do problema",
                "10-25s": "SOLUÇÃO - Como resolver com [PRODUTO]",
                "25-30s": "CTA - Chamada para ação"
            },
            "roteiro": f"""
[TIMESTAMP] DESCRIÇÃO
0:00 - 0:02  VOZ: "Você sabia que a maioria das PMEs falham por falta de gestão de caixa?"
0:02 - 0:05  VIDEO: Gráfico mostrando falências por má gestão
0:05 - 0:12  VOZ: "O problema? Você só descobre que está sem dinheiro quando já é tarde"
0:12 - 0:18  VIDEO: Animação de alertas vermelhos
0:18 - 0:25  VOZ: "A solução é simples: [PRODUTO] te mostra em tempo real"
0:25 - 0:28  VIDEO: Demo do produto
0:28 - 0:30  VOZ: "Comece grátis no link da bio"
            """.strip(),
            "prompt_video": f"Video of entrepreneur checking phone dashboard showing cash flow, worried expression turning to relief",
            "hashtags": ["#fluxocaixa", "#pme", "#finanças", "#startup", "#negócios"],
            "musica_sugestao": "Trending audio - uptempo",
            "tips_producao": [
                "Luz natural是最好的",
                "Fundo organizado profissional",
                "Expressões faciais exageradas",
                "Legendas sempre ativadas"
            ]
        }

    def _obter_template(self, plataforma: str) -> Dict:
        """Obtém template específico da plataforma."""
        templates = {
            "tiktok": {
                "aspect_ratio": "9:16",
                "duramacao_recomendada": "15-30s",
                "estilo": "Casual, autêntico, Trendy",
                "estrutura": "Hook forte → Conteúdo → CTA"
            },
            "instagram": {
                "aspect_ratio": "9:16",
                "duramacao_recomendada": "20-45s",
                "estilo": "Polished mas não production demais",
                "estrutura": "Hook → Story → Solução → CTA"
            },
            "youtube": {
                "aspect_ratio": "9:16",
                "duramacao_recomendada": "30-60s",
                "estilo": "Mais elaborado, educacional",
                "estrutura": "Intro → Problema → Solução → Demo → CTA"
            }
        }
        return templates.get(plataforma, templates["tiktok"])

    def gerar_variacoes(self, tema: str, quantidade: int = 5) -> List[Dict]:
        """Gera múltiplas variações de roteiros."""
        variacoes = []
        for i in range(quantidade):
            variacao = self.gerar_roteiro(tema, duracao=15 + (i * 5))
            variacao["id"] = f"ROT-{tema[:10].upper()}-{i+1:03d}"
            variacoes.append(variacao)
        return variacoes


def main():
    agente = RoteiroShortFormAgent()
    roteiro = agente.gerar_roteiro("O que é fluxo de caixa", 30, "tiktok")
    print(f"Roteiro: {roteiro['tema']}")
    print(f"Gancho: {roteiro['gancho']}")


if __name__ == "__main__":
    main()
