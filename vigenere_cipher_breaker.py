#!/usr/bin/env python3
"""
Vigenère Cipher Breaker
Breaks Vigenère ciphers using Kasiski examination and frequency analysis
"""

import string
import math
from collections import Counter
from frequency_analysis import FrequencyAnalyzer

class VigenereBreaker:
    def __init__(self):
        self.analyzer = FrequencyAnalyzer()
    
    def find_repeated_sequences(self, ciphertext, min_length=3):
        """Find repeated sequences in ciphertext (Kasiski examination)"""
        ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
        sequences = {}
        
        for length in range(min_length, min(20, len(ciphertext) // 4)):
            for i in range(len(ciphertext) - length + 1):
                sequence = ciphertext[i:i + length]
                if sequence in sequences:
                    sequences[sequence].append(i)
                else:
                    sequences[sequence] = [i]
        
        # Filter to only sequences that appear multiple times
        repeated = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
        
        return repeated
    
    def calculate_distances(self, repeated_sequences):
        """Calculate distances between repeated sequences"""
        distances = []
        
        for sequence, positions in repeated_sequences.items():
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    distance = positions[j] - positions[i]
                    distances.append((sequence, distance))
        
        return distances
    
    def find_key_length_candidates(self, distances):
        """Find possible key lengths using GCD of distances"""
        all_distances = [dist for _, dist in distances]
        
        # Count factors of all distances
        factor_counts = Counter()
        
        for distance in all_distances:
            factors = self.get_factors(distance)
            for factor in factors:
                if 2 <= factor <= 20:  # Reasonable key length range
                    factor_counts[factor] += 1
        
        # Return most common factors as key length candidates
        return factor_counts.most_common(10)
    
    def get_factors(self, n):
        """Get all factors of a number"""
        factors = []
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        factors.append(n)
        return factors
    
    def split_into_groups(self, ciphertext, key_length):
        """Split ciphertext into groups based on key position"""
        ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
        groups = ['' for _ in range(key_length)]
        
        for i, char in enumerate(ciphertext):
            groups[i % key_length] += char
        
        return groups
    
    def find_caesar_shift(self, group):
        """Find the most likely Caesar shift for a group using frequency analysis"""
        best_shift = 0
        best_chi_squared = float('inf')
        
        for shift in range(26):
            decrypted = ""
            for char in group:
                shifted = (ord(char) - ord('A') - shift) % 26
                decrypted += chr(shifted + ord('A'))
            
            chi_squared = self.analyzer.calculate_chi_squared(decrypted)
            if chi_squared < best_chi_squared:
                best_chi_squared = chi_squared
                best_shift = shift
        
        return best_shift, best_chi_squared
    
    def decrypt_vigenere(self, ciphertext, key):
        """Decrypt Vigenère cipher with given key"""
        result = ""
        key = key.upper()
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                key_char = key[key_index % len(key)]
                shift = ord(key_char) - ord('A')
                
                if char.isupper():
                    decrypted = (ord(char) - ord('A') - shift) % 26
                    result += chr(decrypted + ord('A'))
                else:
                    decrypted = (ord(char) - ord('a') - shift) % 26
                    result += chr(decrypted + ord('a'))
                
                key_index += 1
            else:
                result += char
        
        return result
    
    def break_vigenere(self, ciphertext):
        """Main function to break Vigenère cipher"""
        print(f"Breaking Vigenère cipher...")
        print(f"Ciphertext: {ciphertext[:100]}...")
        print()
        
        # Step 1: Kasiski examination
        print("1. Kasiski Examination:")
        repeated_sequences = self.find_repeated_sequences(ciphertext)
        
        if not repeated_sequences:
            print("No repeated sequences found. Cipher might be too short or use a one-time pad.")
            return None, None
        
        print("Repeated sequences found:")
        for seq, positions in list(repeated_sequences.items())[:5]:
            print(f"  '{seq}' at positions: {positions}")
        
        distances = self.calculate_distances(repeated_sequences)
        key_length_candidates = self.find_key_length_candidates(distances)
        
        print(f"\nMost likely key lengths:")
        for length, count in key_length_candidates[:5]:
            print(f"  Length {length}: appears {count} times")
        
        # Step 2: Try each key length candidate
        print("\n2. Testing Key Lengths:")
        best_key = ""
        best_plaintext = ""
        best_score = float('inf')
        
        for key_length, _ in key_length_candidates[:5]:
            print(f"\nTesting key length {key_length}:")
            
            groups = self.split_into_groups(ciphertext, key_length)
            key = ""
            total_chi_squared = 0
            
            for i, group in enumerate(groups):
                if len(group) > 0:
                    shift, chi_squared = self.find_caesar_shift(group)
                    key_char = chr((shift) % 26 + ord('A'))
                    key += key_char
                    total_chi_squared += chi_squared
                    print(f"  Group {i+1}: shift {shift} -> '{key_char}' (χ²: {chi_squared:.2f})")
            
            avg_chi_squared = total_chi_squared / len(groups) if groups else float('inf')
            plaintext = self.decrypt_vigenere(ciphertext, key)
            
            print(f"  Key: '{key}'")
            print(f"  Average χ²: {avg_chi_squared:.2f}")
            print(f"  Plaintext preview: {plaintext[:80]}...")
            
            if avg_chi_squared < best_score:
                best_score = avg_chi_squared
                best_key = key
                best_plaintext = plaintext
        
        print("\n" + "="*60)
        print("BEST SOLUTION:")
        print(f"Key: '{best_key}'")
        print(f"Average χ²: {best_score:.2f}")
        print(f"Plaintext: {best_plaintext}")
        
        return best_key, best_plaintext
    
    def index_of_coincidence(self, text):
        """Calculate Index of Coincidence to help determine if text is polyalphabetic"""
        text = ''.join(c for c in text.upper() if c.isalpha())
        if len(text) < 2:
            return 0
        
        letter_counts = Counter(text)
        n = len(text)
        ic = sum(count * (count - 1) for count in letter_counts.values()) / (n * (n - 1))
        
        return ic

def main():
    breaker = VigenereBreaker()
    
    print("Vigenère Cipher Breaker")
    print("Enter encrypted text (or 'quit' to exit):")
    
    while True:
        ciphertext = input("\n> ")
        if ciphertext.lower() == 'quit':
            break
        
        if ciphertext.strip():
            # Check if text might be polyalphabetic
            ic = breaker.index_of_coincidence(ciphertext)
            print(f"Index of Coincidence: {ic:.4f}")
            
            if ic > 0.06:
                print("IC suggests this might be a monoalphabetic cipher (like Caesar or substitution)")
            else:
                print("IC suggests this is likely a polyalphabetic cipher (like Vigenère)")
            
            print()
            key, plaintext = breaker.break_vigenere(ciphertext)
            
            if key:
                print(f"\nFinal Answer:")
                print(f"Key: {key}")
                print(f"Plaintext: {plaintext}")

if __name__ == "__main__":
    main()