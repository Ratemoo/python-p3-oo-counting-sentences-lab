#!/usr/bin/env p

import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        """Returns True if the value ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the value ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Counts the number of sentences in the value."""
        # Define sentence-ending punctuation
        punctuation = '.!?'
        # Replace punctuation marks with a common delimiter
        modified_string = re.sub(f'[{punctuation}]+', '.', self.value)
        # Split by the common delimiter and count non-empty sentences
        sentences = [sentence.strip() for sentence in modified_string.split('.') if sentence.strip()]
        return len(sentences)
