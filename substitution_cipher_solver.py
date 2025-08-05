#!/usr/bin/env python3
"""
Substitution Cipher Solver
Breaks monoalphabetic substitution ciphers using frequency analysis and pattern matching
"""

import string
import re
from collections import Counter, defaultdict
from frequency_analysis import FrequencyAnalyzer

class SubstitutionSolver:
    def __init__(self):
        self.analyzer = FrequencyAnalyzer()
        self.common_words = ['THE', 'AND', 'TO', 'A', 'IN', 'IS', 'IT', 'YOU', 'THAT', 'HE', 'WAS', 'FOR', 'ON', 'ARE', 'AS', 'WITH', 'HIS', 'THEY', 'AT', 'BE', 'THIS', 'OR', 'FROM', 'HAD', 'BY', 'HOT', 'WORD', 'BUT', 'WHAT', 'SOME', 'WE', 'CAN', 'OUT', 'OTHER', 'WERE', 'ALL', 'THERE', 'WHEN', 'UP', 'USE', 'YOUR', 'HOW', 'SAID', 'AN', 'EACH', 'SHE', 'WHICH', 'DO', 'THEIR', 'TIME', 'WILL', 'ABOUT', 'IF', 'UP', 'OUT', 'MANY', 'THEN', 'THEM', 'THESE', 'SO', 'SOME', 'HER', 'WOULD', 'MAKE', 'LIKE', 'INTO', 'HIM', 'HAS', 'TWO', 'MORE', 'GO', 'NO', 'WAY', 'COULD', 'MY', 'THAN', 'FIRST', 'BEEN', 'CALL', 'WHO', 'OIL', 'ITS', 'NOW', 'FIND', 'LONG', 'DOWN', 'DAY', 'DID', 'GET', 'COME', 'MADE', 'MAY', 'PART']
        self.bigrams = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ND', 'ON', 'EN', 'AT', 'OU', 'EA', 'HA', 'NG', 'AS', 'OR', 'TI', 'IS', 'ET', 'IT', 'AR', 'TE', 'ST', 'EN', 'OF']
        self.trigrams = ['THE', 'AND', 'ING', 'HER', 'HAT', 'HIS', 'THA', 'ERE', 'FOR', 'ENT', 'ION', 'TER', 'HAS', 'YOU', 'ITH', 'VER', 'ALL', 'WIT', 'THI', 'TIO']
    
    def get_pattern(self, word):
        """Convert word to pattern (e.g., 'HELLO' -> '01223')"""
        letter_map = {}
        pattern = ""
        next_num = 0
        
        for char in word:
            if char not in letter_map:
                letter_map[char] = str(next_num)
                next_num += 1
            pattern += letter_map[char]
        
        return pattern
    
    def find_pattern_matches(self, cipher_word, word_list):
        """Find words that match the pattern of the cipher word"""
        cipher_pattern = self.get_pattern(cipher_word)
        matches = []
        
        for word in word_list:
            if len(word) == len(cipher_word) and self.get_pattern(word) == cipher_pattern:
                matches.append(word)
        
        return matches
    
    def analyze_patterns(self, ciphertext):
        """Analyze word patterns in the ciphertext"""
        words = re.findall(r'[A-Z]+', ciphertext.upper())
        pattern_analysis = {}
        
        for word in words:
            pattern = self.get_pattern(word)
            if pattern not in pattern_analysis:
                pattern_analysis[pattern] = {
                    'cipher_words': set(),
                    'possible_matches': set()
                }
            pattern_analysis[pattern]['cipher_words'].add(word)
        
        # Find matches for each pattern
        for pattern in pattern_analysis:
            cipher_word = next(iter(pattern_analysis[pattern]['cipher_words']))
            matches = self.find_pattern_matches(cipher_word, self.common_words)
            pattern_analysis[pattern]['possible_matches'] = set(matches)
        
        return pattern_analysis
    
    def build_substitution_key(self, mappings):
        """Build substitution key from letter mappings"""
        key = {}
        reverse_key = {}
        
        for cipher_char, plain_char in mappings.items():
            if cipher_char in key and key[cipher_char] != plain_char:
                return None  # Conflict
            if plain_char in reverse_key and reverse_key[plain_char] != cipher_char:
                return None  # Conflict
            key[cipher_char] = plain_char
            reverse_key[plain_char] = cipher_char
        
        return key
    
    def apply_substitution(self, ciphertext, key):
        """Apply substitution key to decrypt text"""
        result = ""
        for char in ciphertext:
            if char.upper() in key:
                new_char = key[char.upper()]
                result += new_char.lower() if char.islower() else new_char
            else:
                result += char
        return result
    
    def frequency_based_attack(self, ciphertext):
        """Attempt to break cipher using frequency analysis"""
        freq_data = self.analyzer.analyze_text(ciphertext)
        
        # Sort cipher letters by frequency
        cipher_freq = sorted(freq_data.items(), key=lambda x: x[1]['frequency'], reverse=True)
        
        # Sort English letters by frequency
        english_freq = sorted(self.analyzer.english_freq.items(), key=lambda x: x[1], reverse=True)
        
        # Create initial mapping
        initial_key = {}
        for i, (cipher_letter, _) in enumerate(cipher_freq[:10]):  # Top 10 most frequent
            if cipher_letter and i < len(english_freq):
                initial_key[cipher_letter] = english_freq[i][0]
        
        return initial_key
    
    def solve_cipher(self, ciphertext):
        """Main function to solve substitution cipher"""
        print(f"Solving substitution cipher...")
        print(f"Ciphertext: {ciphertext[:100]}...")
        print()
        
        # Frequency analysis
        print("1. Frequency Analysis:")
        freq_key = self.frequency_based_attack(ciphertext)
        print("Initial frequency-based mapping:")
        for cipher, plain in sorted(freq_key.items()):
            print(f"  {cipher} -> {plain}")
        
        freq_result = self.apply_substitution(ciphertext, freq_key)
        freq_chi = self.analyzer.calculate_chi_squared(freq_result)
        print(f"Chi-squared: {freq_chi:.2f}")
        print(f"Partial decrypt: {freq_result[:100]}...")
        print()
        
        # Pattern analysis
        print("2. Pattern Analysis:")
        pattern_analysis = self.analyze_patterns(ciphertext)
        
        print("Word patterns found:")
        for pattern, data in sorted(pattern_analysis.items(), key=lambda x: len(x[1]['cipher_words']), reverse=True)[:5]:
            cipher_words = list(data['cipher_words'])[:3]  # Show first 3
            matches = list(data['possible_matches'])[:3]   # Show first 3
            print(f"  Pattern {pattern}: {cipher_words} -> possible: {matches}")
        
        # Try to build a key from single-letter words and common patterns
        key_mappings = freq_key.copy()
        
        # Look for single letter words (likely 'A' or 'I')
        words = re.findall(r'\b[A-Z]\b', ciphertext.upper())
        if words:
            single_letters = Counter(words)
            most_common_single = single_letters.most_common(1)[0][0]
            key_mappings[most_common_single] = 'A'  # Assume most common single letter is 'A'
        
        final_result = self.apply_substitution(ciphertext, key_mappings)
        final_chi = self.analyzer.calculate_chi_squared(final_result)
        
        print()
        print("Final Results:")
        print("=" * 50)
        print("Substitution key:")
        for cipher, plain in sorted(key_mappings.items()):
            print(f"  {cipher} -> {plain}")
        print(f"Chi-squared: {final_chi:.2f}")
        print(f"Decrypted text: {final_result}")
        
        return key_mappings, final_result

def main():
    solver = SubstitutionSolver()
    
    print("Substitution Cipher Solver")
    print("Enter encrypted text (or 'quit' to exit):")
    
    while True:
        ciphertext = input("\n> ")
        if ciphertext.lower() == 'quit':
            break
        
        if ciphertext.strip():
            key, plaintext = solver.solve_cipher(ciphertext)
            
            print("\nWould you like to manually adjust the key? (y/n)")
            if input("> ").lower() == 'y':
                print("Enter mappings as 'CIPHER_LETTER->PLAIN_LETTER' (or 'done'):")
                while True:
                    mapping = input("mapping> ")
                    if mapping.lower() == 'done':
                        break
                    
                    try:
                        cipher_char, plain_char = mapping.upper().split('->')
                        cipher_char = cipher_char.strip()
                        plain_char = plain_char.strip()
                        key[cipher_char] = plain_char
                        
                        new_result = solver.apply_substitution(ciphertext, key)
                        print(f"Updated result: {new_result[:100]}...")
                    except:
                        print("Invalid format. Use: A->E")

if __name__ == "__main__":
    main()