"""
Agente de SEO e Blog
====================

Arquitetura de agente CrewAI para criar artigos de blog educativos
e otimizados para SEO em múltiplos idiomas.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class SEOBlogAgent:
    """
    Agente especializado em criar conteúdo de blog otimizado para SEO
    que educa e converte no nicho de finanças corporativas.
    """

    def __init__(self):
        self.role = "Especialista em SEO e Conteúdo de Blog"
        self.goal = "Criar artigos de blog que rankeiam para keywords de alto valor e convertem leitores em leads"
        self.backstory = """
        Você é um especialista em SEO e conteúdo com 10 anos de experiência.
        Já criou conteúdo que gerou milhões de visitas orgânicas.
        
        Você domina:
        - SEO on-page e técnica
        - Estratégia de keywords
        - Content clusters
        - Link building
        - Métricas de engajamento
        """

    def criar_agente(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True
        )

    def gerar_artigo(
        self,
        tema: str,
        idioma: str,
        tamanho: str = "medio"
    ) -> Dict[str, Any]:
        """
        Gera artigo completo otimizado para SEO.

        Args:
            tema: Tema do artigo
            idioma: Idioma de destino
            tamanho: Tamanho (curto, medio, longo)

        Returns:
            Dict: Artigo completo com metadados
        """
        keywords = self._identificar_keywords(tema)

        return {
            "id": f"ART-{tema[:10].upper()}-{idioma}",
            "titulo": self._gerar_titulo(tema, idioma),
            "meta_descricao": self._gerar_meta_desc(tema, idioma),
            "keywords_primaria": keywords["primaria"],
            "keywords_secundarias": keywords["secundarias"],
            "slug": self._gerar_slug(tema),
            "estrutura": self._gerar_estrutura(tema, tamanho),
            "conteudo": self._gerar_conteudo_exemplo(tema, idioma),
            "idioma": idioma,
            "tamanho_palavras": {"curto": 800, "medio": 1500, "longo": 2500}[tamanho],
            "tips_seo": self._obter_tips_seo()
        }

    def _identificar_keywords(self, tema: str) -> Dict:
        """Identifica keywords para o tema."""
        keywords_por_tema = {
            "fluxo de caixa": {
                "primaria": "fluxo de caixa",
                "secundarias": [
                    "como fazer fluxo de caixa",
                    "planilha fluxo de caixa",
                    "previsao fluxo de caixa",
                    "gestao fluxo de caixa"
                ],
                "long_tail": [
                    "como fazer fluxo de caixa no excel",
                    "modelo fluxo de caixa mensal",
                    "diferença fluxo de caixa e dre"
                ]
            }
        }
        return keywords_por_tema.get(tema, keywords_por_tema["fluxo de caixa"])

    def _gerar_titulo(self, tema: str, idioma: str) -> str:
        """Gera título otimizado."""
        if idioma == "pt-BR":
            return f"O Guia Completo do Fluxo de Caixa para PMEs em 2026"
        elif idioma == "en-US":
            return f"The Complete Guide to Cash Flow Management for SMBs in 2026"
        return f"[{idioma}] {tema} Guide"

    def _gerar_meta_desc(self, tema: str, idioma: str) -> str:
        """Gera meta descrição."""
        if idioma == "pt-BR":
            return "Aprenda como fazer gestão de fluxo de caixa na prática. Passo a passo com exemplos para PMEs. Comece hoje!"
        elif idioma == "en-US":
            return "Learn how to manage cash flow effectively. Step-by-step guide with examples for SMBs. Start today!"
        return f"{tema} - Complete guide"

    def _gerar_slug(self, tema: str) -> str:
        """Gera slug otimizado."""
        return tema.lower().replace(" ", "-")

    def _gerar_estrutura(self, tema: str, tamanho: str) -> List[str]:
        """Gera estrutura do artigo."""
        return [
            "Introdução (hook + promessa)",
            "O que é fluxo de caixa",
            "Por que é importante",
            "Como fazer passo a passo",
            "Ferramentas recomendadas",
            "Exemplos práticos",
            "Erros comuns a evitar",
            "Conclusão + CTA"
        ]

    def _gerar_conteudo_exemplo(self, tema: str, idioma: str) -> str:
        """Gera exemplo de conteúdo."""
        return f"""
<h1>O que é Fluxo de Caixa?</h1>
<p>O fluxo de caixa é a movimentação de dinheiro dentro e fora da sua empresa.
É diferente do lucro - você pode ter lucro e ainda assim ficar sem dinheiro.</p>

<h2>Por que é importante?</h2>
<p>Estudos mostram que 60% das PMEs fecham nos primeiros 5 anos por falta de 
gestão de caixa. Com [PRODUTO], você evita esse problema.</p>
"""

    def _obter_tips_seo(self) -> List[str]:
        """Retorna tips de SEO on-page."""
        return [
            "Densidade de keyword: 1-2%",
            "Use H1, H2, H3 corretamente",
            "Internal links: 3-5 por artigo",
            "External links: 2-3 para autoridades",
            "Imagens: alt text otimizado",
            "URL: curta e descritiva",
            "Meta title: 50-60 caracteres",
            "Meta description: 150-160 caracteres"
        ]


def main():
    agente = SEOBlogAgent()
    artigo = artigo = agente.gerar_artigo("fluxo de caixa", "pt-BR", "medio")
    print(f"Título: {artigo['titulo']}")
    print(f"Keywords: {artigo['keywords_primaria']}")


if __name__ == "__main__":
    main()
