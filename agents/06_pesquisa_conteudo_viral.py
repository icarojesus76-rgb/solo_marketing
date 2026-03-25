"""
Agente de Pesquisa de Conteúdo Viral
====================================

Arquitetura de agente CrewAI para identificar tendências de Reels, TikTok,
LinkedIn e YouTube relevantes para fluxo de caixa e finanças corporativas.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class PesquisaConteudoViralAgent:
    """
    Agente especializado em identificar tendências de conteúdo viral em
    múltiplas plataformas para o nicho de fluxo de caixa e finanças corporativas.

    Plataformas monitoradas:
    - TikTok
    - Instagram Reels
    - YouTube Shorts
    - LinkedIn Video
    """

    def __init__(self):
        self.role = "Especialista em Pesquisa de Conteúdo Viral"
        self.goal = "Identificar tendências de conteúdo viral e oportunidades de alcance orgânico nas principais plataformas de video para o nicho de finanças corporativas"
        self.backstory = """
        Você é um especialista em marketing de conteúdo viral com 10 anos de 
        experiência em mídias sociais. Formado em Comunicação Digital pela USP,
        você já criou conteúdo que alcançou milhões de visualizações.
        
        Você tem um nariz aguçado para tendências. Você consegue identificar 
        um meme viral antes que ele exploda e sabe exatamente como adaptar 
        tendências gerais para nichos específicos.
        
        No nicho de finanças corporativas, você entende que:
        - O humor pode ser uma porta de entrada para assuntos sérios
        - Gráficos e dados impressionam quando bem apresentados
        - "POV" e Storytelling são extremamente eficazes
        - A educação financeira precisa ser simplificada para viralizar
        
        Sua missão é encontrar o próximo vídeo viral sobre fluxo de caixa 
        antes que nossos concorrentes percebidam.
        """

    def criar_agente(self) -> Agent:
        """Cria e retorna o agente de Pesquisa de Conteúdo Viral."""
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True,
            max_iterations=5
        )

    def monitorar_tendencias(self, plataforma: str) -> List[Dict]:
        """
        Monitora tendências atuais em uma plataforma específica.

        Args:
            plataforma: Nome da plataforma (tiktok, instagram, youtube, linkedin)

        Returns:
            List: Lista de tendências identificadas
        """
        # Em produção, integraria com APIs de tendências
        tendencias_por_plataforma = {
            "tiktok": [
                {
                    "id": "TEND-001",
                    "titulo": "POV: Seu contador te mostra o fluxo de caixa",
                    "hashtags": ["#finanças", "#pme", "#flowdecash"],
                    "potencial_viral": "Alto",
                    "adaptável": True
                },
                {
                    "id": "TEND-002",
                    "titulo": "Trend de antes/depois com gráficos",
                    "hashtags": ["#transformation", "#growth"],
                    "potencial_viral": "Médio",
                    "adaptável": True
                },
                {
                    "id": "TEND-003",
                    "titulo": "Explicando fluxo de caixa em 30 segundos",
                    "hashtags": ["#education", "#finance"],
                    "potencial_viral": "Alto",
                    "adaptável": True
                }
            ],
            "instagram": [
                {
                    "id": "TEND-004",
                    "titulo": "Reels de tips rápidos financeiros",
                    "hashtags": ["#financast", "#dicasfinanceiras"],
                    "potencial_viral": "Alto",
                    "adaptável": True
                },
                {
                    "id": "TEND-005",
                    "titulo": "Carrossel educativo sobre fluxo de caixa",
                    "hashtags": ["#educaçãofinanceira", "#pmebr"],
                    "potencial_viral": "Médio",
                    "adaptável": True
                }
            ],
            "youtube": [
                {
                    "id": "TEND-006",
                    "titulo": "Shorts de erros comuns em gestão de caixa",
                    "hashtags": ["#shorts", "#finanças"],
                    "potencial_viral": "Alto",
                    "adaptável": True
                }
            ],
            "linkedin": [
                {
                    "id": "TEND-007",
                    "titulo": "Posts sobre burnout financeiro de CFOs",
                    "hashtags": ["#CFO", "#finançascorporativas"],
                    "potencial_viral": "Médio",
                    "adaptável": True
                }
            ]
        }

        return tendencias_por_plataforma.get(plataforma, [])

    def identificar_oportunidades(self, nicho: str) -> List[Dict]:
        """
        Identifica oportunidades de conteúdo para um nicho específico.

        Args:
            nicho: Nicho de conteúdo (ex: 'fluxo de caixa PME')

        Returns:
            List: Oportunidades identificadas
        """
        oportunidades = [
            {
                "tipo": "Educacional",
                "titulo": "O que é fluxo de caixa em 60 segundos",
                "formato": "Short-form video",
                "dificuldade": "Fácil",
                "potencial_alcance": "Alto",
                "investimento": "Baixo"
            },
            {
                "tipo": "Storytelling",
                "titulo": "Como o fluxo de caixa salvou 3 PMEs",
                "formato": "Case de sucesso",
                "dificuldade": "Média",
                "potencial_alcance": "Médio",
                "investimento": "Médio"
            },
            {
                "tipo": "Entretenimento",
                "titulo": "Reação de donos ao ver seu fluxo de caixa",
                "formato": "POV/Reação",
                "dificuldade": "Fácil",
                "potencial_alcance": "Alto",
                "investimento": "Baixo"
            },
            {
                "tipo": "Interativo",
                "titulo": "Quiz: Você sabe quanto tem no caixa?",
                "formato": "Enquetes/Qizzes",
                "dificuldade": "Fácil",
                "potencial_alcance": "Médio",
                "investimento": "Baixo"
            },
            {
                "tipo": "Viral",
                "titulo": "POV: Você descobre que ia falir (com fluxo de caixa)",
                "formato": "Storytelling",
                "dificuldade": "Média",
                "potencial_alcance": "Muito Alto",
                "investimento": "Médio"
            }
        ]

        logger.info(
            f"Identificadas {len(oportunidades)} oportunidades para '{nicho}'")
        return oportunidades

    def analisar_heatmaps(self, plataforma: str) -> Dict[str, Any]:
        """
        Analisa heatmaps de engajamento por horário e tema.

        Args:
            plataforma: Plataforma a analisar

        Returns:
            Dict: Análise de melhores horários e temas
        """
        heatmaps = {
            "tiktok": {
                "melhores_horarios": ["12:00-14:00", "18:00-20:00", "21:00-23:00"],
                "dias_melhores": ["Terça", "Quarta", "Quinta"],
                "temas_quentes": [
                    "Educação financeira",
                    "Lifestyle empresarial",
                    "Tips rápidos",
                    "POV de escritório"
                ]
            },
            "instagram": {
                "melhores_horarios": ["08:00-10:00", "12:00-13:00", "19:00-21:00"],
                "dias_melhores": ["Segunda", "Terça", "Quarta"],
                "temas_quentes": [
                    "Dicas práticas",
                    "Gráficos好看的",
                    "Carrosséis educativos"
                ]
            },
            "youtube": {
                "melhores_horarios": ["12:00-15:00", "18:00-21:00"],
                "dias_melhores": ["Sábado", "Domingo", "Quarta"],
                "temas_quentes": [
                    "Tutoriais completos",
                    "Análises de casos",
                    "Comparativos"
                ]
            },
            "linkedin": {
                "melhores_horarios": ["07:00-09:00", "12:00-13:00", "17:00-18:00"],
                "dias_melhores": ["Segunda", "Terça", "Quarta", "Quinta"],
                "temas_quentes": [
                    "Insights profissionais",
                    "Dados e estatísticas",
                    "Thought leadership"
                ]
            }
        }

        return heatmaps.get(plataforma, {})

    def gerar_recomendacoes(self, plataforma: str) -> List[str]:
        """
        Gera recomendações de conteúdo para uma plataforma.

        Args:
            plataforma: Plataforma alvo

        Returns:
            List: Recomendações de conteúdo
        """
        recomendacoes = {
            "tiktok": [
                "Use hooks nos primeiros 2 segundos",
                "Legendas essenciais (85% assiste sem som)",
                "Trendy audio + educational content = viral",
                "Challenge: #FluxoDeCaixaChallenge"
            ],
            "instagram": [
                "Reels com CTA claro",
                "Stories para bastidores",
                "Carrosséis para conteúdo denso",
                "Engaje nos comentários"
            ],
            "youtube": [
                "Thumbnail com expressão + texto",
                "Hook na descrição + primeiros 30s",
                "CTAs nos cards e end screen",
                "Playlist de shorts + vídeos longos"
            ],
            "linkedin": [
                "Opens com pergunta provocativa",
                "Dados com fonte citada",
                "Formato: Problema → Solução → CTA",
                "Engaje com comentários primeiro"
            ]
        }

        return recomendacoes.get(plataforma, [])


def main():
    """Função de teste do agente."""
    agente = PesquisaConteudoViralAgent()

    print("=== Tendências TikTok ===")
    tendencias = agente.monitorar_tendencias("tiktok")
    for t in tendencias[:2]:
        print(f"- {t['titulo']} ({t['potencial_viral']})")

    print("\n=== Oportunidades ===")
    opp = agente.identificar_oportunidades("fluxo de caixa PME")
    print(f"Encontradas {len(opp)} oportunidades")

    print("\n=== Recomendações YouTube ===")
    rec = agente.gerar_recomendacoes("youtube")
    for r in rec:
        print(f"- {r}")


if __name__ == "__main__":
    main()
