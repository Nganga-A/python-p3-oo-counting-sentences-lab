#!/usr/bin/env python3
import re #regular expressions


class MyString:
      def __init__(self, value=""):
            self.value = None
            self.set_value(value)

      def get_value(self):
            return self._value

      def set_value(self, new_value):
            if isinstance(new_value, str):
                  self._value = new_value
            else:
                  print("The value must be a string.")

      def is_sentence(self):
            return self._value.endswith('.')

      def is_question(self):
            return self._value.endswith('?')

      def is_exclamation(self):
            return self._value.endswith('!')

      def count_sentences(self):
            pattern = r'[.!?]' #regular expression split pattern
            sentences = re.split(pattern, self._value)
            print(sentences)
            sentences = [sentence for sentence in sentences if sentence.strip()] #strip removes whitespaces
            return(len(sentences))

      value = property(get_value, set_value)

string = MyString("")
string.value = "This is a string! It has three sentences. Right?"
string.count_sentences()