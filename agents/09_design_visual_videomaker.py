"""
Agente de Design Visual e Videomaker
====================================

Arquitetura de agente CrewAI para gerar prompts de IA para imagem e vídeo
com layout otimizado para redes sociais.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class DesignVisualVideomakerAgent:
    """
    Agente especializado em criar prompts para ferramentas de IA generativa
    (DALL-E, Midjourney, Sora, Runway) otimizados para conteúdo de marketing.
    """

    def __init__(self):
        self.role = "Diretor de Arte e Videomaker Digital"
        self.goal = "Criar prompts de design e vídeo que geram assets visuais profissionais usando IA generativa"
        self.backstory = """
        Você é um diretor de arte digital com 10 anos de experiência em 
        branding e produção visual para marcas B2B.
        
        Você domina as melhores práticas de criação de prompts para:
        - Imagens: DALL-E, Midjourney, Stable Diffusion
        - Vídeos: Sora, Runway, Pika Labs
        - Editores: Canva, CapCut, Figma
        
        Você entende que cada plataforma tem suas especificações visuais
        e sabe otimizar prompts para cada contexto.
        """

    def criar_agente(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True
        )

    def gerar_prompt_imagem(
        self,
        conceito: str,
        estilo: str,
        plataforma: str
    ) -> Dict[str, Any]:
        """
        Gera prompt otimizado para geração de imagem.

        Args:
            conceito: Conceito visual desejado
            estilo: Estilo visual (moderno, minimalista, etc)
            plataforma: Plataforma de destino

        Returns:
            Dict: Prompt e configurações
        """
        return {
            "id": f"IMG-{conceito[:5].upper()}",
            "conceito": conceito,
            "prompt_principal": self._construir_prompt(conceito, estilo),
            "estilo": estilo,
            "plataforma": plataforma,
            "dimensoes": self._obter_dimensoes(plataforma),
            "tips": [
                "Use referências de artistas específicos",
                "Inclua detalhes de iluminação",
                "Especifique o mood emocional",
                "Evite texto em inglês nos prompts"
            ]
        }

    def _construir_prompt(self, conceito: str, estilo: str) -> str:
        """Constrói prompt otimizado."""
        base = f"{conceito}, {estilo} style"
        modificadores = "professional lighting, high quality, 4K"
        return f"{base}, {modificadores}"

    def _obter_dimensoes(self, plataforma: str) -> str:
        """Obtém dimensões corretas por plataforma."""
        dimensoes = {
            "instagram_post": "1080x1080",
            "instagram_story": "1080x1920",
            "linkedin": "1200x627",
            "tiktok": "1080x1920",
            "twitter": "1600x900"
        }
        return dimensoes.get(plataforma, "1080x1080")

    def gerar_prompt_video(self, tipo: str, duracao: int) -> Dict[str, Any]:
        """
        Gera prompt para geração de vídeo via IA.

        Args:
            tipo: Tipo de vídeo (demo, testimonial, etc)
            duracao: Duração em segundos

        Returns:
            Dict: Prompt e configurações de vídeo
        """
        templates = {
            "demo": {
                "prompt": "Professional software demo screen recording style, clean UI, arrow animations pointing to key features",
                "duracao": "30-60s",
                "ferramenta": "Runway / Sora"
            },
            "testimonial": {
                "prompt": "Professional testimonial video setup, warm lighting, happy business person talking",
                "duracao": "30-60s",
                "ferramenta": "Runway"
            },
            "explainer": {
                "prompt": "Animated whiteboard explainer style, hand drawing financial graphs and charts",
                "duracao": "60-90s",
                "ferramenta": "Runway / D-ID"
            }
        }

        return {
            "id": f"VID-{tipo.upper()}",
            "tipo": tipo,
            "prompt": templates.get(tipo, templates["demo"])["prompt"],
            "duracao": duracao,
            "ferramenta_recomendada": templates.get(tipo, {})["ferramenta"],
            "formato": "MP4",
            "resolucao": "1080x1920 ou 1920x1080"
        }

    def gerar_assets_kit(self, marca: str) -> List[Dict]:
        """Gera kit completo de assets para marca."""
        return [
            {"tipo": "Logo", "formato": "PNG/SVG", "uso": "Assinatura em posts"},
            {"tipo": "Paleta", "formato": "HEX codes", "uso": "Consistência visual"},
            {"tipo": "Templates", "formato": "Canva/Figma", "uso": "Posts rápidos"},
            {"tipo": "Fontes", "formato": "OTF/TTF", "uso": "Materiais oficiais"}
        ]


def main():
    agente = DesignVisualVideomakerAgent()
    prompt = agente.gerar_prompt_imagem(
        "Dashboard de fluxo de caixa", "modern", "instagram")
    print(f"Prompt gerado: {prompt['prompt_principal']}")


if __name__ == "__main__":
    main()
