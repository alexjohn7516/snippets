from django.test import TestCase
from .models import Question

class QuestionTestCase(TestCase):
    def testQuestion(self):
        question = Question(question_text="What is your name?", pub_date="12/12/12")
        self.assertEqual(question.question_text, "What is your name?")
        self.assertEqual(question.pub_date, '12/12/12')