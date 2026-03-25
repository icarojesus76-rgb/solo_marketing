"""
Agente de Copys e Legendas Social
=================================

Arquitetura de agente CrewAI para escrever legendas, CTAs, hashtags
e textos de video para cada canal e idioma.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class CopysLegendasSocialAgent:
    """
    Agente especializado em criar copywriting persuasivo para mídias sociais
    adaptado para cada plataforma e idioma.
    """

    def __init__(self):
        self.role = "Copywriter Especialista em Mídias Sociais"
        self.goal = "Criar copys, legendas e CTAs irresistíveis que convertem engajamento em leads qualificados"
        self.backstory = """
        Você é um copywriter especialista em mídias sociais com 12 anos de 
        experiência criando textos que viralizam e convertem.
        
        Você domina a arte de escrever para diferentes plataformas, entendendo
        que cada uma tem seu próprio linguajar e melhores práticas.
        
        Você acredita que boas copys:
        - Começam com um gancho que para o scroll
        - Criam urgência sem parecer desesperado
        - Oferecem valor antes de pedir algo
        - Usam linguagem natural e conversacional
        """

    def criar_agente(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True
        )

    def gerar_legenda(
        self,
        tema: str,
        plataforma: str,
        idioma: str = "pt-BR"
    ) -> Dict[str, Any]:
        """
        Gera legenda completa para post.

        Args:
            tema: Tema do post
            plataforma: Plataforma alvo
            idioma: Idioma do texto

        Returns:
            Dict: Legenda com todos os elementos
        """
        templates = {
            "tiktok": {
                "formato": "Curta, impactante, com emoji",
                "caracteres": "150-200",
                "estrutura": "Hook → Contexto → CTA"
            },
            "instagram": {
                "formato": "Mais elaborada, com quebra de linha",
                "caracteres": "150-300",
                "estrutura": "Hook → 正文 → Hashtags → CTA"
            },
            "linkedin": {
                "formato": "Profissional, mas não chato",
                "caracteres": "150-300",
                "estrutura": "Insight → Dados → Opinião → CTA"
            }
        }

        config = templates.get(plataforma, templates["instagram"])

        return {
            "id": f"LEG-{plataforma.upper()}-{tema[:5].upper()}",
            "plataforma": plataforma,
            "idioma": idioma,
            "legenda": self._gerar_texto(tema, plataforma, idioma),
            "hashtags": self._gerar_hashtags(tema, plataforma),
            "cta": self._gerar_cta(tema, plataforma),
            "emoji_utilizados": ["📊", "💰", "✅", "🔥"],
            "caracteres": "150-200",
            "formato": config
        }

    def _gerar_texto(self, tema: str, plataforma: str, idioma: str) -> str:
        """Gera texto da legenda."""
        if idioma == "pt-BR":
            return f"""📊 {tema}

Você sabia que a maioria das PMEs brasileiras não conseguem prever seu fluxo de caixa?

Isso é perigoso.

Sem visibilidade, você:
• Perde prazos de pagamento
• Não sabe se pode contratar
• Descobre os problemas tarde demais

A solução?

[PRODUTO] mostra seu caixa em tempo real, com IA que aprende seu negócio.

👉 Comece grátis no link da bio."""
        return f"[{idioma}] {tema} caption"

    def _gerar_hashtags(self, tema: str, plataforma: str) -> List[str]:
        """Gera hashtags relevantes."""
        base = ["#fluxocaixa", "#pme", "#finanças", "#gestão"]
        if plataforma == "tiktok":
            base.extend(["#tiktokbusiness", "#viral"])
        elif plataforma == "linkedin":
            base.extend(["#CFO", "#finançascorporativas"])
        return base[:10]

    def _gerar_cta(self, tema: str, plataforma: str) -> str:
        """Gera call-to-action."""
        ctas = {
            "tiktok": "▶️ Salvem pra ver depois | 👉 Link na bio",
            "instagram": "💬 Comenta aqui | 📩 Manda DM | 🔗 Link na bio",
            "linkedin": "💬 Qual sua experiência? | 🔗 Leia mais"
        }
        return ctas.get(plataforma, "👉 Link na bio")

    def gerar_sequencia_copys(self, tipo_campanha: str) -> List[Dict]:
        """Gera sequência de copys para campanha."""
        sequencias = {
            "lancamento": [
                {"dia": 1, "tipo": "Awareness", "copy": "Temos algo novo..."},
                {"dia": 3, "tipo": "Intriga", "copy": "Está quase pronto..."},
                {"dia": 5, "tipo": "Prévia", "copy": "Olha só o que vem..."},
                {"dia": 7, "tipo": "Lançamento", "copy": "CHEGOU! 🚀"}
            ],
            "black_friday": [
                {"dia": 1, "tipo": "Countdown", "copy": "Falta X dias..."},
                {"dia": 3, "tipo": "Teaser", "copy": "Oferta especial..."},
                {"dia": 5, "tipo": "Urgência", "copy": "Amanhã é o dia!"},
                {"dia": 6, "tipo": "Black Friday", "copy": "50% OFF! ⏰"}
            ]
        }
        return sequencias.get(tipo_campanha, sequencias["lancamento"])


def main():
    agente = CopysLegendasSocialAgent()
    legenda = agente.gerar_legenda("Fluxo de Caixa", "instagram")
    print(f"Legenda gerada: {len(legenda['legenda'])} caracteres")


if __name__ == "__main__":
    main()
