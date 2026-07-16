sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae los títulos de una lista de artículos."""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:  # Solo títulos con más de 10 caracteres
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae los títulos de una lista de artículos usando comprensión de listas."""
    return [article["title"] for article in articles if len(article["title"]) > 10]


def extract_article_summary(articles):
    """Extrae un resumen de cada artículo con título y fuente."""
    return {article["title"]: article["description"] for article in articles}


print(extract_titles_traditional(sample_articles))
print("====")
print(extract_titles(sample_articles))
print("====")
print(extract_article_summary(sample_articles))


def get_sources_trad(articles):
    """Obtiene una lista de fuentes únicas de los artículos."""

    sources = []
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.append(article.get("source").get("name"))
    return sources


def get_sources(articles):
    """Obtiene una lista de fuentes únicas de los artículos usando comprensión de listas."""
    return [
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    ]


print(get_sources_trad(sample_articles))
print("====")
print(get_sources(sample_articles))


def categorize_traditional(articles):
    """Categoriza los artículos por su categoría."""
    sources = get_sources(articles)
    categories = {}
    for source in sources:
        if source not in categories:
            categories[source] = []
        for article in articles:
            if source == article.get("source").get("name"):
                categories[source].append(article)
    return categories


def categorizar(articles):
    """Categoriza los artículos por su categoría usando comprensión de listas."""
    sources = get_sources(articles)
    return {
        source: [
            article
            for article in articles
            if article.get("source").get("name") == source
        ]
        for source in sources
    }


print(categorize_traditional(sample_articles))
print("====")
print(categorizar(sample_articles))
