"""
📄 TEST PAPER GENERATOR - Create Mock Tests with AI Questions
"""

import random
from typing import List, Optional, Dict
from datetime import datetime
from models import QuestionModel, TestPaperModel, Subject, DifficultyLevel
import config
from src.tools.maths_tool import MathsTool

class TestPaperGenerator:
    """Generate complete test papers"""
    
    def __init__(self):
        self.maths_tool = MathsTool()
        self.sessions = config.SESSIONS
        self.subjects = config.SUBJECTS
    
    def generate_full_mock_test(
        self,
        session: str = "SESSION_1",
        language: str = "Hindi"
    ) -> TestPaperModel:
        """Generate full SSC MTS mock test (100 questions)"""
        
        print(f"📝 Generating Full Mock Test for {session}...")
        
        session_config = self.sessions[session]
        total_questions = session_config["total_questions"]
        questions_per_subject = total_questions // 4  # 25 each
        
        all_questions = []
        
        # Generate questions from each subject
        for subject_name, subject_config in self.subjects.items():
            print(f"  📐 Generating {subject_name} questions...")
            
            if subject_name == "MATHS":
                qs = self._generate_maths_questions(questions_per_subject)
            elif subject_name == "REASONING":
                qs = self._generate_reasoning_questions(questions_per_subject)
            elif subject_name == "GENERAL_AWARENESS":
                qs = self._generate_ga_questions(questions_per_subject)
            elif subject_name == "ENGLISH":
                qs = self._generate_english_questions(questions_per_subject)
            
            all_questions.extend(qs)
        
        # Shuffle questions
        random.shuffle(all_questions)
        
        # Create test paper
        paper = TestPaperModel(
            paper_id=f"MOCK_{session}_{int(datetime.now().timestamp())}",
            session=session,
            total_questions=len(all_questions),
            questions=all_questions,
            duration_minutes=120,
            total_marks=100,
            negative_marking=session_config["negative_marking"],
            difficulty_distribution=config.DIFFICULTY_DISTRIBUTION
        )
        
        print(f"✅ Generated {len(all_questions)} questions")
        return paper
    
    def generate_subject_wise_test(
        self,
        subject: str,
        count: int = 25,
        session: str = "SESSION_1"
    ) -> TestPaperModel:
        """Generate subject-specific test"""
        
        print(f"📚 Generating {subject} test...")
        
        if subject == "MATHS":
            questions = self._generate_maths_questions(count)
        elif subject == "REASONING":
            questions = self._generate_reasoning_questions(count)
        elif subject == "GENERAL_AWARENESS":
            questions = self._generate_ga_questions(count)
        elif subject == "ENGLISH":
            questions = self._generate_english_questions(count)
        else:
            questions = []
        
        random.shuffle(questions)
        
        paper = TestPaperModel(
            paper_id=f"{subject}_{session}_{int(datetime.now().timestamp())}",
            session=session,
            total_questions=len(questions),
            questions=questions,
            duration_minutes=30,
            total_marks=25,
            negative_marking=self.sessions[session]["negative_marking"],
            difficulty_distribution=config.DIFFICULTY_DISTRIBUTION
        )
        
        return paper
    
    def generate_topic_wise_test(
        self,
        subject: str,
        topic: str,
        count: int = 10
    ) -> TestPaperModel:
        """Generate topic-specific practice test"""
        
        print(f"🎯 Generating {subject} - {topic} practice test...")
        
        questions = []
        
        # Generate questions with different difficulties
        for difficulty in [DifficultyLevel.EASY, DifficultyLevel.MEDIUM, DifficultyLevel.HARD]:
            qs = self._generate_questions_by_difficulty(
                subject, topic, difficulty, count // 3
            )
            questions.extend(qs)
        
        random.shuffle(questions)
        
        paper = TestPaperModel(
            paper_id=f"{subject}_{topic}_{int(datetime.now().timestamp())}",
            session="PRACTICE",
            total_questions=len(questions),
            questions=questions,
            duration_minutes=15,
            total_marks=count,
            negative_marking=False,
            difficulty_distribution=config.DIFFICULTY_DISTRIBUTION
        )
        
        return paper
    
    def _generate_maths_questions(self, count: int) -> List[QuestionModel]:
        """Generate Maths questions with difficulty balance"""
        
        maths_topics = self.subjects["MATHS"]["topics"]
        questions = []
        
        # Easy questions (33%)
        easy_count = int(count * config.DIFFICULTY_DISTRIBUTION["Easy"])
        for _ in range(easy_count):
            topic = random.choice(maths_topics)
            q = self.maths_tool.generator.generate_questions(
                topic=topic,
                difficulty=DifficultyLevel.EASY,
                count=1,
                language="Hindi"
            )
            questions.extend(q)
        
        # Medium questions (34%)
        medium_count = int(count * config.DIFFICULTY_DISTRIBUTION["Medium"])
        for _ in range(medium_count):
            topic = random.choice(maths_topics)
            q = self.maths_tool.generator.generate_questions(
                topic=topic,
                difficulty=DifficultyLevel.MEDIUM,
                count=1,
                language="Hindi"
            )
            questions.extend(q)
        
        # Hard questions (33%)
        hard_count = count - easy_count - medium_count
        for _ in range(hard_count):
            topic = random.choice(maths_topics)
            q = self.maths_tool.generator.generate_questions(
                topic=topic,
                difficulty=DifficultyLevel.HARD,
                count=1,
                language="Hindi"
            )
            questions.extend(q)
        
        return questions[:count]
    
    def _generate_reasoning_questions(self, count: int) -> List[QuestionModel]:
        """Generate Reasoning questions"""
        # TODO: Implement Reasoning Tool
        print("⚠️ Reasoning Tool not yet implemented")
        return []
    
    def _generate_ga_questions(self, count: int) -> List[QuestionModel]:
        """Generate General Awareness questions"""
        # TODO: Implement GA Tool
        print("⚠️ GA Tool not yet implemented")
        return []
    
    def _generate_english_questions(self, count: int) -> List[QuestionModel]:
        """Generate English questions"""
        # TODO: Implement English Tool
        print("⚠️ English Tool not yet implemented")
        return []
    
    def _generate_questions_by_difficulty(
        self,
        subject: str,
        topic: str,
        difficulty: DifficultyLevel,
        count: int
    ) -> List[QuestionModel]:
        """Generate questions by difficulty level"""
        # Generic implementation
        return []


class TestPaperExporter:
    """Export test papers in different formats"""
    
    @staticmethod
    def export_to_pdf(paper: TestPaperModel, filename: str):
        """Export to PDF"""
        print(f"📄 Exporting to PDF: {filename}")
        # TODO: Implement PDF export using ReportLab
        pass
    
    @staticmethod
    def export_to_json(paper: TestPaperModel, filename: str):
        """Export to JSON"""
        import json
        print(f"📋 Exporting to JSON: {filename}")
        
        data = {
            "paper_id": paper.paper_id,
            "session": paper.session,
            "total_questions": paper.total_questions,
            "questions": [q.dict() for q in paper.questions],
            "duration_minutes": paper.duration_minutes,
            "total_marks": paper.total_marks,
            "negative_marking": paper.negative_marking
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    
    @staticmethod
    def export_to_csv(paper: TestPaperModel, filename: str):
        """Export to CSV"""
        import csv
        print(f"📊 Exporting to CSV: {filename}")
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                "Question#", "Subject", "Topic", "Difficulty",
                "Question(Hindi)", "Option A", "Option B", "Option C", "Option D", "Answer"
            ])
            
            for idx, q in enumerate(paper.questions, 1):
                writer.writerow([
                    idx,
                    q.subject,
                    q.topic,
                    q.difficulty,
                    q.question_text_hi,
                    q.options[0] if len(q.options) > 0 else "",
                    q.options[1] if len(q.options) > 1 else "",
                    q.options[2] if len(q.options) > 2 else "",
                    q.options[3] if len(q.options) > 3 else "",
                    q.correct_answer
                ])


if __name__ == "__main__":
    # Test Paper Generator
    generator = TestPaperGenerator()
    
    # Generate full mock test
    paper = generator.generate_full_mock_test(session="SESSION_1", language="Hindi")
    
    # Export in different formats
    exporter = TestPaperExporter()
    exporter.export_to_json(paper, "mock_test_session1.json")
    exporter.export_to_csv(paper, "mock_test_session1.csv")
    # exporter.export_to_pdf(paper, "mock_test_session1.pdf")
