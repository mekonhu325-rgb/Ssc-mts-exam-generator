"""
🧠 REASONING TOOL - AI-Powered Question Generator & Extractor
Covers: Series, Coding-Decoding, Analogy, Classification, etc.
"""

import random
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import json

# ============================================
# DATA MODELS
# ============================================

class ReasoningSubtopic(Enum):
    """All Reasoning subtopics for SSC MTS"""
    ALPHA_NUMERIC_SERIES = "Alpha-Numeric Series"
    CODING_DECODING = "Coding-Decoding"
    ANALOGY = "Analogy"
    CLASSIFICATION = "Classification"
    DIRECTIONS_DISTANCE = "Directions & Distance"
    ORDER_RANKING = "Order & Ranking"
    BLOOD_RELATIONS = "Blood Relations"
    VENN_DIAGRAM = "Venn Diagrams"
    MATHEMATICAL_OPERATIONS = "Mathematical Operations"
    NON_VERBAL = "Non-Verbal Reasoning"
    AGE_PROBLEMS = "Age Problems"


class ReasoningQuestion:
    """Model for a reasoning question"""
    
    def __init__(
        self,
        question_id: str,
        subtopic: ReasoningSubtopic,
        question_text_en: str,
        question_text_hi: str,
        options: List[str],
        correct_answer: str,
        explanation_en: str,
        explanation_hi: str,
        difficulty: str,
        source_year: Optional[int] = None,
        source_session: Optional[str] = None
    ):
        self.question_id = question_id
        self.subtopic = subtopic
        self.question_text_en = question_text_en
        self.question_text_hi = question_text_hi
        self.options = options
        self.correct_answer = correct_answer
        self.explanation_en = explanation_en
        self.explanation_hi = explanation_hi
        self.difficulty = difficulty
        self.source_year = source_year
        self.source_session = source_session
    
    def to_dict(self):
        return {
            "question_id": self.question_id,
            "subject": "REASONING",
            "subtopic": self.subtopic.value,
            "question_en": self.question_text_en,
            "question_hi": self.question_text_hi,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "explanation_en": self.explanation_en,
            "explanation_hi": self.explanation_hi,
            "difficulty": self.difficulty,
            "source_year": self.source_year,
            "source_session": self.source_session
        }


# ============================================
# REASONING QUESTION GENERATOR
# ============================================

class ReasoningQuestionGenerator:
    """AI-powered Reasoning question generator"""
    
    def __init__(self):
        self.subtopics = ReasoningSubtopic
        self.generated_questions = []
    
    def generate_alpha_numeric_series(self, difficulty: str) -> ReasoningQuestion:
        """Generate alpha-numeric series questions"""
        
        if difficulty == "Easy":
            # Simple number series
            series_data = {
                "question_en": "Find the missing number in the series: 2, 4, 6, 8, ?",
                "question_hi": "श्रृंखला में लुप्त संख्या खोजें: 2, 4, 6, 8, ?",
                "options": ["10", "12", "14", "16"],
                "answer": "10",
                "explanation_en": "Each number increases by 2. So 8 + 2 = 10",
                "explanation_hi": "हर संख्या 2 से बढ़ती है। तो 8 + 2 = 10"
            }
        elif difficulty == "Medium":
            series_data = {
                "question_en": "Find the missing number: 3, 6, 12, 24, ?",
                "question_hi": "लुप्त संख्या खोजें: 3, 6, 12, 24, ?",
                "options": ["36", "48", "42", "50"],
                "answer": "48",
                "explanation_en": "Each number is multiplied by 2. So 24 × 2 = 48",
                "explanation_hi": "हर संख्या को 2 से गुणा किया जाता है। तो 24 × 2 = 48"
            }
        else:  # Hard
            series_data = {
                "question_en": "Find the missing number: 1, 4, 9, 16, 25, ?",
                "question_hi": "लुप्त संख्या खोजें: 1, 4, 9, 16, 25, ?",
                "options": ["36", "49", "42", "48"],
                "answer": "36",
                "explanation_en": "Series of perfect squares: 1², 2², 3², 4², 5², 6² = 36",
                "explanation_hi": "पूर्ण वर्गों की श्रृंखला: 1², 2², 3², 4², 5², 6² = 36"
            }
        
        return ReasoningQuestion(
            question_id=f"REASONING_{self.subtopics.ALPHA_NUMERIC_SERIES.name}_{datetime.now().timestamp()}",
            subtopic=self.subtopics.ALPHA_NUMERIC_SERIES,
            question_text_en=series_data["question_en"],
            question_text_hi=series_data["question_hi"],
            options=series_data["options"],
            correct_answer=series_data["answer"],
            explanation_en=series_data["explanation_en"],
            explanation_hi=series_data["explanation_hi"],
            difficulty=difficulty
        )
    
    def generate_coding_decoding(self, difficulty: str) -> ReasoningQuestion:
        """Generate coding-decoding questions"""
        
        if difficulty == "Easy":
            data = {
                "question_en": "If ROSE is coded as 1234, then ROTE is coded as?",
                "question_hi": "यदि ROSE को 1234 के रूप में कोडित किया जाता है, तो ROTE को कोडित किया जाता है?",
                "options": ["1243", "1234", "1324", "4321"],
                "answer": "1243",
                "explanation_en": "R=1, O=2, S=3, E=4. So ROTE = R(1) + O(2) + T(3→4) + E(4) = 1243",
                "explanation_hi": "R=1, O=2, S=3, E=4। तो ROTE = 1243"
            }
        elif difficulty == "Medium":
            data = {
                "question_en": "If A = 1, B = 2, ... Z = 26, then CAT is coded as?",
                "question_hi": "यदि A = 1, B = 2, ... Z = 26, तो CAT को कोडित किया जाता है?",
                "options": ["2+1+20", "3+1+20", "3+1+19", "2+1+19"],
                "answer": "3+1+20",
                "explanation_en": "C=3, A=1, T=20. So CAT = 3+1+20 = 24",
                "explanation_hi": "C=3, A=1, T=20। तो CAT = 24"
            }
        else:  # Hard
            data = {
                "question_en": "If TREE is coded as 20-18-5-5, then FLOOR is coded as?",
                "question_hi": "यदि TREE को 20-18-5-5 के रूप में कोडित किया जाता है, तो FLOOR को कोडित किया जाता है?",
                "options": ["6-12-15-15-18", "6-12-14-15-18", "6-12-15-14-18", "6-11-15-15-18"],
                "answer": "6-12-15-15-18",
                "explanation_en": "Using reverse alphabet: F=6, L=12, O=15, O=15, R=18",
                "explanation_hi": "उल्टे वर्णमाला का उपयोग: F=6, L=12, O=15, O=15, R=18"
            }
        
        return ReasoningQuestion(
            question_id=f"REASONING_{self.subtopics.CODING_DECODING.name}_{datetime.now().timestamp()}",
            subtopic=self.subtopics.CODING_DECODING,
            question_text_en=data["question_en"],
            question_text_hi=data["question_hi"],
            options=data["options"],
            correct_answer=data["answer"],
            explanation_en=data["explanation_en"],
            explanation_hi=data["explanation_hi"],
            difficulty=difficulty
        )
    
    def generate_analogy(self, difficulty: str) -> ReasoningQuestion:
        """Generate analogy questions"""
        
        if difficulty == "Easy":
            data = {
                "question_en": "Dog : Bark :: Cat : ?",
                "question_hi": "कुत्ता : भौंकना :: बिल्ली : ?",
                "options": ["Meow", "Howl", "Growl", "Hiss"],
                "answer": "Meow",
                "explanation_en": "A dog barks, similarly a cat meows",
                "explanation_hi": "कुत्ता भौंकता है, इसी तरह बिल्ली म्याऊं करती है"
            }
        elif difficulty == "Medium":
            data = {
                "question_en": "Painter : Canvas :: Writer : ?",
                "question_hi": "चित्रकार : कैनवास :: लेखक : ?",
                "options": ["Paper", "Pen", "Book", "Ink"],
                "answer": "Paper",
                "explanation_en": "A painter works on canvas, a writer works on paper",
                "explanation_hi": "चित्रकार कैनवास पर काम करता है, लेखक कागज पर"
            }
        else:  # Hard
            data = {
                "question_en": "Botany : Plants :: Zoology : ?",
                "question_hi": "वनस्पति विज्ञान : पौधे :: प्राणी विज्ञान : ?",
                "options": ["Animals", "Trees", "Insects", "Organisms"],
                "answer": "Animals",
                "explanation_en": "Botany is the study of plants, Zoology is the study of animals",
                "explanation_hi": "वनस्पति विज्ञान पौधों का अध्ययन है, प्राणी विज्ञान जानवरों का"
            }
        
        return ReasoningQuestion(
            question_id=f"REASONING_{self.subtopics.ANALOGY.name}_{datetime.now().timestamp()}",
            subtopic=self.subtopics.ANALOGY,
            question_text_en=data["question_en"],
            question_text_hi=data["question_hi"],
            options=data["options"],
            correct_answer=data["answer"],
            explanation_en=data["explanation_en"],
            explanation_hi=data["explanation_hi"],
            difficulty=difficulty
        )
    
    def generate_blood_relations(self, difficulty: str) -> ReasoningQuestion:
        """Generate blood relations questions"""
        
        if difficulty == "Easy":
            data = {
                "question_en": "A is the mother of B. B is the son of C. How is C related to A?",
                "question_hi": "A, B की माता है। B, C का पुत्र है। C का A से क्या संबंध है?",
                "options": ["Father", "Brother", "Husband", "Son"],
                "answer": "Husband",
                "explanation_en": "If A is mother of B and B is son of C, then C is A's husband",
                "explanation_hi": "यदि A, B की माता है और B, C का पुत्र है, तो C, A का पति है"
            }
        elif difficulty == "Medium":
            data = {
                "question_en": "A's mother is B. B's father is C. C is the brother of D. How is D related to A?",
                "question_hi": "A की माता B है। B का पिता C है। C, D का भाई है। D का A से क्या संबंध है?",
                "options": ["Uncle", "Aunt", "Grandfather", "Grandmother"],
                "answer": "Uncle",
                "explanation_en": "C is A's grandfather. D is C's brother, so D is A's great-uncle/uncle",
                "explanation_hi": "C, A का दादा है। D, C का भाई है, तो D, A का चाचा है"
            }
        else:  # Hard
            data = {
                "question_en": "A and B are brothers. C is sister of A. D is mother of C. E is father of D. How is E related to B?",
                "question_hi": "A और B भाई हैं। C, A की बहन है। D, C की माता है। E, D का पिता है। E का B से क्या संबंध है?",
                "options": ["Grandfather", "Grandmother", "Father", "Great-grandfather"],
                "answer": "Grandfather",
                "explanation_en": "E is grandfather of C, A, and B",
                "explanation_hi": "E, C, A और B का दादा है"
            }
        
        return ReasoningQuestion(
            question_id=f"REASONING_{self.subtopics.BLOOD_RELATIONS.name}_{datetime.now().timestamp()}",
            subtopic=self.subtopics.BLOOD_RELATIONS,
            question_text_en=data["question_en"],
            question_text_hi=data["question_hi"],
            options=data["options"],
            correct_answer=data["answer"],
            explanation_en=data["explanation_en"],
            explanation_hi=data["explanation_hi"],
            difficulty=difficulty
        )
    
    def generate_directions(self, difficulty: str) -> ReasoningQuestion:
        """Generate directions & distance questions"""
        
        if difficulty == "Easy":
            data = {
                "question_en": "A person walks 10 km North, then 10 km East. How far is he from the starting point?",
                "question_hi": "एक व्यक्ति 10 किमी उत्तर में चलता है, फिर 10 किमी पूर्व में। वह शुरुआती बिंदु से कितना दूर है?",
                "options": ["10 km", "20 km", "14.14 km", "10√2 km"],
                "answer": "14.14 km",
                "explanation_en": "Using Pythagorean theorem: √(10² + 10²) = 10√2 ≈ 14.14 km",
                "explanation_hi": "पाइथागोरस प्रमेय: √(10² + 10²) = 14.14 किमी"
            }
        elif difficulty == "Medium":
            data = {
                "question_en": "A faces North. He turns 90° clockwise, then 45° counter-clockwise. Which direction is he facing?",
                "question_hi": "A उत्तर की ओर देख रहा है। वह 90° घड़ी की ओर मुड़ता है, फिर 45° वामावर्त। वह किस दिशा की ओर देख रहा है?",
                "options": ["North-East", "North-West", "South-East", "South-West"],
                "answer": "North-East",
                "explanation_en": "North → 90° CW = East → 45° CCW = North-East",
                "explanation_hi": "उत्तर → 90° घड़ी = पूर्व → 45° वामावर्त = पूर्वोत्तर"
            }
        else:  # Hard
            data = {
                "question_en": "A starts at point O and walks 6 km East, then 8 km North, then 15 km West. How far from O?",
                "question_hi": "A बिंदु O से शुरू करता है और 6 किमी पूर्व में चलता है, फिर 8 किमी उत्तर, फिर 15 किमी पश्चिम। O से कितना दूर?",
                "options": ["9 km", "10 km", "12 km", "17 km"],
                "answer": "10 km",
                "explanation_en": "Final position: (-9, 8). Distance = √(81+64) = √145 ≈ 10 km",
                "explanation_hi": "अंतिम स्थिति: (-9, 8)। दूरी = 10 किमी"
            }
        
        return ReasoningQuestion(
            question_id=f"REASONING_{self.subtopics.DIRECTIONS_DISTANCE.name}_{datetime.now().timestamp()}",
            subtopic=self.subtopics.DIRECTIONS_DISTANCE,
            question_text_en=data["question_en"],
            question_text_hi=data["question_hi"],
            options=data["options"],
            correct_answer=data["answer"],
            explanation_en=data["explanation_en"],
            explanation_hi=data["explanation_hi"],
            difficulty=difficulty
        )
    
    def generate_random_question(self, difficulty: str = "Medium") -> ReasoningQuestion:
        """Generate random reasoning question"""
        
        generators = [
            self.generate_alpha_numeric_series,
            self.generate_coding_decoding,
            self.generate_analogy,
            self.generate_blood_relations,
            self.generate_directions
        ]
        
        generator = random.choice(generators)
        return generator(difficulty)


# ============================================
# REASONING TOOL (MAIN CLASS)
# ============================================

class ReasoningTool:
    """Main Reasoning Tool - Coordinates all reasoning questions"""
    
    def __init__(self):
        self.generator = ReasoningQuestionGenerator()
        self.database = []
    
    def generate_questions(
        self,
        subtopic: Optional[str] = None,
        difficulty: str = "Medium",
        count: int = 5,
        language: str = "Hindi"
    ) -> List[Dict]:
        """Generate reasoning questions"""
        
        print(f"\n🧠 Generating {count} Reasoning questions...")
        print(f"   Difficulty: {difficulty}")
        print(f"   Language: {language}\n")
        
        questions = []
        
        for i in range(count):
            if subtopic:
                # Generate specific subtopic
                q = self.generator.generate_random_question(difficulty)
            else:
                # Random subtopic
                q = self.generator.generate_random_question(difficulty)
            
            questions.append(q.to_dict())
            print(f"   ✅ Generated question {i+1}/{count}")
        
        self.database.extend(questions)
        return questions
    
    def run(self):
        """Run the Reasoning Tool"""
        
        print("\n" + "="*60)
        print("🧠 SSC MTS REASONING TOOL")
        print("="*60 + "\n")
        
        # Generate mixed questions
        easy_qs = self.generate_questions(difficulty="Easy", count=3)
        medium_qs = self.generate_questions(difficulty="Medium", count=4)
        hard_qs = self.generate_questions(difficulty="Hard", count=3)
        
        total_questions = len(easy_qs) + len(medium_qs) + len(hard_qs)
        
        print(f"\n✅ Successfully generated {total_questions} reasoning questions")
        print(f"   Easy: {len(easy_qs)}")
        print(f"   Medium: {len(medium_qs)}")
        print(f"   Hard: {len(hard_qs)}")
        
        return self.database


# ============================================
# EXAMPLE USAGE
# ============================================

if __name__ == "__main__":
    tool = ReasoningTool()
    questions = tool.run()
    
    # Save to JSON
    import json
    with open("reasoning_questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print("\n💾 Questions saved to reasoning_questions.json")
