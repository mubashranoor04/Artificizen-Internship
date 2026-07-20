#Create a ChromaDB in-memory collection, add 10 short paragraphs from any topic, query it with a natural language question, and print the top-2 results.
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.create_collection("demo")

documents = [
    """A marine biologist spent six months studying coral reefs in the Indian Ocean.
    The research showed that healthy coral ecosystems support thousands of marine species
    and protect coastlines from erosion.""",

    """FastAPI is a modern Python web framework designed for building high-performance APIs.
    It uses type hints for automatic validation and generates interactive API documentation
    without requiring additional configuration.""",

    """A historian discovered handwritten letters from the nineteenth century in an old library.
    The letters revealed details about daily life, local trade, and cultural traditions that
    had never been documented before.""",

    """Electric vehicles use rechargeable battery packs instead of gasoline engines.
    They produce no tailpipe emissions and require regular charging through compatible
    charging stations.""",

    """Machine learning enables computers to identify patterns in large datasets.
    Businesses use these models for fraud detection, recommendation systems,
    demand forecasting, and customer behavior analysis.""",

    """The International Space Station orbits Earth approximately every ninety minutes.
    Astronauts aboard the station perform scientific experiments that help researchers
    understand how humans adapt to microgravity.""",

    """A cybersecurity analyst monitors network traffic to detect suspicious activity.
    Encryption, multi-factor authentication, and regular software updates reduce
    the risk of unauthorized access and data breaches.""",

    """Urban planners design cities that balance transportation, housing, and public spaces.
    Well-planned bicycle lanes, parks, and efficient public transit improve the quality
    of life for residents while reducing traffic congestion.""",

    """Beekeepers maintain healthy bee colonies because bees are essential pollinators.
    Many fruits, vegetables, and flowering plants rely on pollination to produce
    seeds and maintain agricultural productivity.""",

    """Cloud computing allows organizations to rent computing resources over the internet
    instead of maintaining expensive physical servers. Companies can quickly scale
    storage and processing power based on changing business needs."""
]

embeddings = model.encode(documents)

collection.add(
    ids=[str(i) for i in range(len(documents))],
    documents=documents,
    embeddings=embeddings.tolist()
)

query = "Which Python framework is commonly used to build REST APIs?"

query_embedding = model.encode(query)

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)

print(results["documents"])