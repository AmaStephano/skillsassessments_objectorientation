"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1 - Abstraction
   		You can hide details of the implementation that the users don't need to understand or access.   
   
   2 - Encapsulation
   		Data and the functions that manipulate the data are kept together. This makes it easier to keep track of everything.

   3 - Polymorphism
   		You can easily interchange compoments. You can call the same methods on different instances without have to write new code.
   		Also, you can have different implementations of the same methods.  

2. What is a class?
	A class is a blueprint for an object. It decsribes how you can make something. It can include methods and subclasses. 
   You can create lots of different instances of an object. They will all vary in some manner, but will maintain a certain level of consistency.  

3. What is an instance attribute?
	It is an attribute created at the instance level. It is unique to that instance and can not be changed by any other instance.

4. What is a method?
	
	They are similar to functions, but are defined inside a class. It takes a class instance as its first parameter. 

5. What is an instance in object orientation?
	An instance is an occurence of a class that happens is created when you run the program. It doesn't exist before then. 

6. How is a class attribute different than an instance attribute?
   	A class atrribute is defined at the class level and is applied to all instances. 
      A instance attribute is defined at the instance level and is unique to that instance.

   	An example of class attributes would be if you had a car class and all cars had a gas attribute that you wanted to start the same level. 
      An example of an insteance attribute would be type. 
      You would want to set that at the instance attribute level to indicate if it is a truck, sedan, compact, etc. Since this will vary a lot


"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):

   def __init__(self, first_name, last_name, address):
      self.first_name = first_name
      self.last_name = last_name
      self.address = address


class Question(object):

   def __init__(self, question, correct_answer):
      self.question = question
      self.correct_answer = correct_answer


   def ask_and_evaluate(self):
      answer = raw_input("%s > " % (self.question))
      if answer == self.correct_answer:
         return True
      else:
         return False


class Exam(object):

   def __init__(self, name):
      self.name = name
      self.questions = []


   def add_question(self, question, answer):
      new_question = Question(question, answer)
      self.questions.append(new_question)


   def administer(self):
      score = 0
      for q in self.questions:
         if q.ask_and_evaluate() == True:
            score += 1
      return score


class Quiz(Exam):

   def administer(self):
      score = super(Quiz, self).administer()
      num_of_questions = len(self.questions)
      if score < num_of_questions / 2:
         return False
      else:
         return True


def take_test(exam, student):
   score = exam.administer()
   student.score = score


def example():
   exam = Exam("Midterm")
   exam.add_question("What is the method for adding an element to a set?", ".add()")
   exam.add_question("What is the method for adding an element to a list", ".append()")

   student1 = Student("Amanda", "Stephano", "267 San Jose Ave")
   take_test(exam, student1)
   print "%s's score is %s" % (student1.first_name, student1.score)


def quiz_example():
   quiz = Quiz("Midterm")
   quiz.add_question("What is the method for adding an element to a set?", ".add()")
   quiz.add_question("What is the method for adding an element to a list", ".append()")

   student1 = Student("Amanda", "Stephano", "267 San Jose Ave")
   take_test(quiz, student1)
   print "%s %s" % (student1.first_name, student1.score)



