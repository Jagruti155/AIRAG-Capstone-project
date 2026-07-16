import os, sys
from dotenv import load_dotenv
from openai import OpenAI

# Load OPENAI_API_KEY from the environment — never hard-code keys
load_dotenv()
client = OpenAI(base_url="https://openai.vocareum.com/v1",)

def ask(question, history) :
    history.append({"role": "user", "content": question})
    answer = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history,
    )

    history.append({"role": "assistant", "content": answer.choices[0].message.content})
    return answer.choices[0].message.content

def main():
    conversation_history = [
        {
            "role": "system", 
            "content": "You are an experienced software engineer having 5+ years of experience."
        }
    ]
    
    # --- TURN 1 ---
    print("--- Turn 1 ---")
    q1 = "I'm working on a security project where I want to build agentAI for detecting vulnerabilities. Can you give me some ideas for the project? Also the project name is Proactive AI Bot (PAB)."
    print(f"User: {q1}")
    
    reply1 = ask(q1, conversation_history)
    print(f"AI: {reply1}\n")
    
    # --- TURN 2 (The Memory Test) ---
    print("--- Turn 2 ---")
    # We ask a question that CANNOT be answered unless the AI remembers Turn 1
    q2 = "Be honest, do you think my security project will be tricky and lengthy to implement? Also, what was my project name again?"
    print(f"User: {q2}")
    
    reply2 = ask(q2, conversation_history)
    print(f"AI: {reply2}")

if __name__ == "__main__":
    main()


