
# Function to build context from retrieved chunks for LLM input (LLM Expects input in text format, not in a list of chunks)
# as retrieved chunks are not in a single document format and need to be formatted for LLM input

def build_context(retrieved_chunks):
    context_parts = []

    for chunk in retrieved_chunks:
        source = chunk["source"]
        text = chunk["text"]

        # format each chunk with its source and text, separated by a newline
        context_part = f"Source: {source}\n{text}"
        context_parts.append(context_part)

    # Join all context parts with a double newline
    context = "\n\n".join(context_parts)

    return context