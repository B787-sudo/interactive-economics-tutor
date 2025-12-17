def answer_question(question, context):
    question = question.lower()

    if "economics" in question:
        return (
            "Economics is a social science that studies how people use limited "
            "resources to satisfy their unlimited wants. It focuses on production, "
            "distribution, and consumption of goods and services."
        )

    if "scarcity" in question:
        return (
            "Scarcity means that resources are limited while human wants are unlimited. "
            "Because of scarcity, choices must be made about how resources are used."
        )

    if "opportunity cost" in question:
        return (
            "Opportunity cost is the value of the next best alternative that is given up "
            "when a choice is made."
        )

    if "summarize" in question or "summary" in question:
        return (
            "This chapter introduces economics as a subject, explains scarcity, "
            "opportunity cost, and the basic economic problems of what to produce, "
            "how to produce, and for whom to produce."
        )

    # fallback answer
    return (
        "This question is related to the economics chapter. "
        "Please refer to the chapter concepts like scarcity, choice, and opportunity cost."
    )
