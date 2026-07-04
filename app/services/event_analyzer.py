from transformers import pipeline

# Load the zero-shot classification model once
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# Default candidate themes
DEFAULT_LABELS = [
    "Artificial Intelligence",
    "Healthcare",
    "Blockchain",
    "Education",
    "Sustainability",
    "Cybersecurity",
    "Cloud Computing",
    "Agriculture",
    "Finance",
    "Data Science",
    "Machine Learning",
    "Networking",
    "Urban Planning"
]


def analyze_event(description: str, candidate_labels: list = None):
    """
    Extract the top 3 themes from an event description.
    """

    if candidate_labels is None:
        candidate_labels = DEFAULT_LABELS

    result = classifier(
        description,
        candidate_labels=candidate_labels
    )

    return result["labels"][:3]