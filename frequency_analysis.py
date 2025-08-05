#!/usr/bin/env python3
"""
Frequency Analysis Utilities for Cryptanalysis
Educational tool for analyzing letter frequencies in encrypted text
"""

import string
from collections import Counter
import math

class FrequencyAnalyzer:
    def __init__(self):
        # English letter frequencies (percentage)
        self.english_freq = {
            'A': 8.12, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.02, 'F': 2.23,
            'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03,
            'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93, 'Q': 0.10, 'R': 5.99,
            'S': 6.33, 'T': 9.06, 'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15,
            'Y': 1.97, 'Z': 0.07
        }
    
    def analyze_text(self, text):
        """Analyze frequency of letters in given text"""
        text = text.upper()
        letters_only = ''.join(c for c in text if c.isalpha())
        
        if not letters_only:
            return {}
        
        letter_count = Counter(letters_only)
        total_letters = len(letters_only)
        
        frequency_data = {}
        for letter in string.ascii_uppercase:
            count = letter_count.get(letter, 0)
            frequency_data[letter] = {
                'count': count,
                'frequency': (count / total_letters) * 100 if total_letters > 0 else 0
            }
        
        return frequency_data
    
    def calculate_chi_squared(self, text):
        """Calculate chi-squared statistic to measure how close text is to English"""
        freq_data = self.analyze_text(text)
        letters_only = ''.join(c for c in text.upper() if c.isalpha())
        total_letters = len(letters_only)
        
        chi_squared = 0
        for letter in string.ascii_uppercase:
            observed = freq_data[letter]['count']
            expected = (self.english_freq[letter] / 100) * total_letters
            if expected > 0:
                chi_squared += ((observed - expected) ** 2) / expected
        
        return chi_squared
    
    def display_frequency_table(self, text):
        """Display frequency analysis in a readable format"""
        freq_data = self.analyze_text(text)
        
        print("Letter Frequency Analysis")
        print("=" * 50)
        print(f"{'Letter':<6} {'Count':<6} {'Freq%':<8} {'Expected%':<10} {'Diff':<8}")
        print("-" * 50)
        
        for letter in string.ascii_uppercase:
            count = freq_data[letter]['count']
            frequency = freq_data[letter]['frequency']
            expected = self.english_freq[letter]
            diff = frequency - expected
            
            if count > 0:
                print(f"{letter:<6} {count:<6} {frequency:<8.2f} {expected:<10.2f} {diff:<8.2f}")
    
    def get_most_common_letters(self, text, n=5):
        """Get the n most common letters in the text"""
        freq_data = self.analyze_text(text)
        sorted_letters = sorted(freq_data.items(), key=lambda x: x[1]['count'], reverse=True)
        return [(letter, data['count'], data['frequency']) for letter, data in sorted_letters[:n] if data['count'] > 0]

def main():
    analyzer = FrequencyAnalyzer()
    
    print("Frequency Analysis Tool")
    print("Enter text to analyze (or 'quit' to exit):")
    
    while True:
        text = input("\n> ")
        if text.lower() == 'quit':
            break
        
        if text.strip():
            analyzer.display_frequency_table(text)
            chi_squared = analyzer.calculate_chi_squared(text)
            print(f"\nChi-squared statistic: {chi_squared:.2f}")
            print("(Lower values indicate text closer to English)")
            
            most_common = analyzer.get_most_common_letters(text)
            print(f"\nMost common letters:")
            for i, (letter, count, freq) in enumerate(most_common, 1):
                print(f"{i}. {letter}: {count} occurrences ({freq:.2f}%)")

if __name__ == "__main__":
    main()