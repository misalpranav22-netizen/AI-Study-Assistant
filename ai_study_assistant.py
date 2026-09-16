# ==========================================
# AI Study Assistant
# Module 5 - AI Tools & Mini Project
# ==========================================

def generate_study_help(topic):
    print("\n" + "=" * 50)
    print("AI STUDY ASSISTANT")
    print("=" * 50)

    print(f"\nTopic: {topic}")

    print("\n1. SIMPLE EXPLANATION")
    print(f"{topic} is an important topic that can be understood by learning its basic concepts, working process, and practical applications.")

    print("\n2. KEY POINTS")
    print(f"- Understand the basic concepts of {topic}")
    print(f"- Learn how {topic} works")
    print(f"- Study practical examples of {topic}")
    print(f"- Practice questions related to {topic}")

    print("\n3. STUDY TIP")
    print(f"Start with the fundamentals of {topic}, then move to examples and practical implementation.")

    print("\n4. INTERVIEW QUESTIONS")
    print(f"- What is {topic}?")
    print(f"- How does {topic} work?")
    print(f"- What are the applications of {topic}?")

    print("\n5. REVISION")
    print(f"Revise the main concepts of {topic} and try explaining them in your own words.")

    print("=" * 50)


def main():
    print("Welcome to AI Study Assistant!")

    topic = input("\nEnter the topic you want to study: ")

    if topic.strip() == "":
        print("Please enter a valid topic.")
    else:
        generate_study_help(topic)


if __name__ == "__main__":
    main()
