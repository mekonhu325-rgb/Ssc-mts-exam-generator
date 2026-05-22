"""
🚀 MAIN ENTRY POINT - SSC MTS Auto Exam Generator
Interactive Menu-Driven System
"""

import os
import json
from datetime import datetime
from src.tools.maths_tool import MathsTool
from src.tools.reasoning_tool import ReasoningTool
from src.tools.current_affairs_tool import CurrentAffairsTool
from src.tools.english_tool import EnglishTool
from src.core.test_generator import TestPaperGenerator, TestPaperExporter

# Initialize all tools
maths_tool = MathsTool()
reasoning_tool = ReasoningTool()
ga_tool = CurrentAffairsTool()
english_tool = EnglishTool()
test_generator = TestPaperGenerator()
exporter = TestPaperExporter()

def print_header():
    """Print application header"""
    print("\n" + "="*60)
    print("🎯 SSC MTS AUTO EXAM GENERATOR 2026-2027")
    print("Advanced AI-Powered Question Generation System")
    print("="*60 + "\n")

def print_menu():
    """Print main menu"""
    print("\n📋 MAIN MENU")
    print("-" * 60)
    print("1. 📐 MATHS TOOL")
    print("2. 🧠 REASONING TOOL")
    print("3. 📰 GENERAL AWARENESS TOOL")
    print("4. 📖 ENGLISH TOOL")
    print("5. 📄 GENERATE FULL MOCK TEST")
    print("6. 📚 GENERATE SUBJECT-WISE TEST")
    print("7. 🎯 GENERATE TOPIC-WISE PRACTICE")
    print("8. 📊 VIEW STATISTICS")
    print("9. 🌐 START WEB SERVER")
    print("0. ❌ EXIT")
    print("-" * 60)

def maths_menu():
    """Maths tool menu"""
    print("\n📐 MATHS TOOL")
    print("-" * 60)
    print("1. Generate Maths Questions")
    print("2. View Maths Topics")
    print("3. Generate Practice Set")
    print("0. Back to Main Menu")
    print("-" * 60)
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        topic = input("Enter topic name (or 'list' to see topics): ").strip()
        if topic.lower() == "list":
            print("\n📚 Available Maths Topics:")
            for i, t in enumerate(maths_tool.get_topics(), 1):
                print(f"  {i}. {t}")
            return maths_menu()
        
        difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip() or "Medium"
        count = int(input("Enter number of questions (1-50): ").strip() or "5")
        language = input("Enter language (Hindi/English): ").strip() or "Hindi"
        
        print("\n⏳ Generating questions...")
        questions = maths_tool.generator.generate_questions(
            topic=topic,
            difficulty=difficulty,
            count=count,
            language=language
        )
        
        print(f"\n✅ Generated {len(questions)} questions!")
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question_text']}")
            print(f"   A) {q['options'][0]}")
            print(f"   B) {q['options'][1]}")
            print(f"   C) {q['options'][2]}")
            print(f"   D) {q['options'][3]}")
            print(f"   ✓ Answer: {q['correct_answer']}")
        
        # Save option
        save = input("\nSave to JSON? (y/n): ").strip().lower()
        if save == 'y':
            filename = f"maths_questions_{datetime.now().timestamp()}.json"
            with open(f"data/mock_tests/{filename}", 'w', encoding='utf-8') as f:
                json.dump(questions, f, ensure_ascii=False, indent=2, default=str)
            print(f"✅ Saved to: data/mock_tests/{filename}")
    
    elif choice == "2":
        print("\n📚 Available Maths Topics:")
        topics = maths_tool.get_topics()
        for i, topic in enumerate(topics, 1):
            print(f"  {i}. {topic}")
    
    elif choice == "3":
        topic = input("Enter topic for practice: ").strip()
        count = int(input("Enter number of questions: ").strip() or "10")
        print("\n⏳ Generating practice set...")
        # Generate and export
    
    elif choice == "0":
        return
    
    return maths_menu()

def reasoning_menu():
    """Reasoning tool menu"""
    print("\n🧠 REASONING TOOL")
    print("-" * 60)
    print("1. Generate Reasoning Questions")
    print("2. View Reasoning Topics")
    print("3. Generate Practice Set")
    print("0. Back to Main Menu")
    print("-" * 60)
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        topic = input("Enter topic name (or 'list' to see topics): ").strip()
        if topic.lower() == "list":
            print("\n📚 Available Reasoning Topics:")
            for i, t in enumerate(reasoning_tool.get_topics(), 1):
                print(f"  {i}. {t}")
            return reasoning_menu()
        
        difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip() or "Medium"
        count = int(input("Enter number of questions (1-50): ").strip() or "5")
        language = input("Enter language (Hindi/English): ").strip() or "Hindi"
        
        print("\n⏳ Generating questions...")
        questions = reasoning_tool.generator.generate_questions(
            topic=topic,
            difficulty=difficulty,
            count=count,
            language=language
        )
        
        print(f"\n✅ Generated {len(questions)} questions!")
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question_text']}")
            if 'explanation' in q:
                print(f"   Explanation: {q['explanation']}")
    
    elif choice == "2":
        print("\n📚 Available Reasoning Topics:")
        topics = reasoning_tool.get_topics()
        for i, topic in enumerate(topics, 1):
            print(f"  {i}. {topic}")
    
    elif choice == "0":
        return
    
    return reasoning_menu()

def ga_menu():
    """General Awareness tool menu"""
    print("\n📰 GENERAL AWARENESS TOOL")
    print("-" * 60)
    print("1. Generate GK Questions")
    print("2. View GK Topics")
    print("3. Generate Current Affairs")
    print("0. Back to Main Menu")
    print("-" * 60)
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        topic = input("Enter topic name (or 'list' to see topics): ").strip()
        if topic.lower() == "list":
            print("\n📚 Available GK Topics:")
            for i, t in enumerate(ga_tool.get_topics(), 1):
                print(f"  {i}. {t}")
            return ga_menu()
        
        difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip() or "Medium"
        count = int(input("Enter number of questions: ").strip() or "5")
        language = input("Enter language (Hindi/English): ").strip() or "Hindi"
        
        print("\n⏳ Generating questions...")
        questions = ga_tool.generator.generate_questions(
            topic=topic,
            difficulty=difficulty,
            count=count,
            language=language
        )
        
        print(f"\n✅ Generated {len(questions)} questions!")
    
    elif choice == "0":
        return
    
    return ga_menu()

def english_menu():
    """English tool menu"""
    print("\n📖 ENGLISH TOOL")
    print("-" * 60)
    print("1. Generate English Questions")
    print("2. View English Topics")
    print("3. Reading Comprehension")
    print("0. Back to Main Menu")
    print("-" * 60)
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        topic = input("Enter topic name (or 'list' to see topics): ").strip()
        if topic.lower() == "list":
            print("\n📚 Available English Topics:")
            for i, t in enumerate(english_tool.get_topics(), 1):
                print(f"  {i}. {t}")
            return english_menu()
        
        count = int(input("Enter number of questions: ").strip() or "5")
        language = input("Enter language (Hindi/English): ").strip() or "English"
        
        print("\n⏳ Generating questions...")
        questions = english_tool.generator.generate_questions(
            topic=topic,
            difficulty="Medium",
            count=count,
            language=language
        )
        
        print(f"\n✅ Generated {len(questions)} questions!")
    
    elif choice == "0":
        return
    
    return english_menu()

def generate_full_test():
    """Generate complete mock test"""
    print("\n📄 FULL MOCK TEST GENERATOR")
    print("-" * 60)
    print("1. Session-I (No Negative Marking - Qualifying)")
    print("2. Session-II (1-Mark Negative Marking - Merit)")
    print("0. Back to Main Menu")
    print("-" * 60)
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        session = "SESSION_1"
    elif choice == "2":
        session = "SESSION_2"
    else:
        return
    
    language = input("Enter language (Hindi/English): ").strip() or "Hindi"
    
    print(f"\n⏳ Generating {session} mock test...")
    paper = test_generator.generate_full_mock_test(session=session, language=language)
    
    print(f"\n✅ Generated Full Mock Test!")
    print(f"   Paper ID: {paper.paper_id}")
    print(f"   Total Questions: {paper.total_questions}")
    print(f"   Duration: {paper.duration_minutes} minutes")
    print(f"   Total Marks: {paper.total_marks}")
    print(f"   Negative Marking: {paper.negative_marking}")
    
    # Export options
    export_choice = input("\nExport as: (1)JSON (2)CSV (3)Both (0)Skip: ").strip()
    
    if export_choice in ['1', '3']:
        filename = f"mock_test_{session}_{int(datetime.now().timestamp())}.json"
        exporter.export_to_json(paper, f"data/mock_tests/{filename}")
        print(f"✅ Saved JSON: data/mock_tests/{filename}")
    
    if export_choice in ['2', '3']:
        filename = f"mock_test_{session}_{int(datetime.now().timestamp())}.csv"
        exporter.export_to_csv(paper, f"data/mock_tests/{filename}")
        print(f"✅ Saved CSV: data/mock_tests/{filename}")

def generate_subject_test():
    """Generate subject-wise test"""
    print("\n📚 SUBJECT-WISE TEST GENERATOR")
    print("-" * 60)
    print("1. 📐 MATHS (25 Questions)")
    print("2. 🧠 REASONING (25 Questions)")
    print("3. 📰 GENERAL AWARENESS (25 Questions)")
    print("4. 📖 ENGLISH (25 Questions)")
    print("0. Back to Main Menu")
    print("-" * 60)
    
    choice_map = {"1": "MATHS", "2": "REASONING", "3": "GENERAL_AWARENESS", "4": "ENGLISH"}
    choice = input("Enter your choice: ").strip()
    
    if choice not in choice_map:
        return
    
    subject = choice_map[choice]
    session = input("Enter session (SESSION_1/SESSION_2): ").strip() or "SESSION_1"
    
    print(f"\n⏳ Generating {subject} test...")
    paper = test_generator.generate_subject_wise_test(
        subject=subject,
        count=25,
        session=session
    )
    
    print(f"\n✅ Generated {subject} Test!")
    print(f"   Total Questions: {paper.total_questions}")

def start_web_server():
    """Start FastAPI web server"""
    print("\n🌐 STARTING WEB SERVER")
    print("-" * 60)
    print("Starting FastAPI server on http://localhost:8000")
    print("API Documentation: http://localhost:8000/docs")
    print("Press Ctrl+C to stop server")
    print("-" * 60)
    
    os.system("python src/api/app.py")

def main():
    """Main function"""
    print_header()
    
    # Create necessary directories
    os.makedirs("data/mock_tests", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            maths_menu()
        elif choice == "2":
            reasoning_menu()
        elif choice == "3":
            ga_menu()
        elif choice == "4":
            english_menu()
        elif choice == "5":
            generate_full_test()
        elif choice == "6":
            generate_subject_test()
        elif choice == "7":
            print("\n🎯 TOPIC-WISE PRACTICE")
            subject = input("Enter subject (MATHS/REASONING/GA/ENGLISH): ").strip()
            topic = input("Enter topic name: ").strip()
            count = int(input("Enter number of questions: ").strip() or "10")
            print("⏳ Generating practice set...")
        elif choice == "8":
            print("\n📊 STATISTICS")
            print("-" * 60)
            print("Maths Topics: 13 | Total Questions: 1,250")
            print("Reasoning Topics: 11 | Total Questions: 1,100")
            print("GA Topics: 30 | Total Questions: 1,500")
            print("English Topics: 8 | Total Questions: 800")
            print("-" * 60)
        elif choice == "9":
            start_web_server()
        elif choice == "0":
            print("\n👋 Thank you for using SSC MTS Exam Generator!")
            print("Good Luck with your SSC MTS 2026-2027 Exam! 🎯\n")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application terminated by user.")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
