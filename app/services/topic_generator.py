from transformers import pipeline, set_seed

# Set seed for reproducible results
set_seed(42)

# Load GPT-2 Small model once
generator = pipeline(
    "text-generation",
    model="gpt2"
)


def generate_topics(themes: list[str], interests: list[str]) -> list[str]:
    """
    Generate professional conversation starters
    based on event themes and user interests.
    """

    prompt = (
        f"I am attending a networking event about {', '.join(themes)}. "
        f"My interests are {', '.join(interests)}.\n"
        f"Generate exactly 3 professional conversation starters:\n"
        "1."
    )

    result = generator(
        prompt,
        max_length=80,
        num_return_sequences=1,
        temperature=0.8,
        do_sample=True,
        truncation=True
    )

    generated_text = result[0]["generated_text"]

    # Remove the original prompt
    generated_text = generated_text.replace(prompt, "").strip()

    suggestions = []

    for line in generated_text.split("\n"):
        line = line.strip()

        if not line:
            continue

        # Remove numbering or bullet points
        line = line.lstrip("1234567890.-• ")

        if line:
            suggestions.append(line)

    # If GPT-2 didn't generate separate lines,
    # return the generated text as one suggestion.
    if not suggestions:
        suggestions.append(generated_text)

    return suggestions[:3]