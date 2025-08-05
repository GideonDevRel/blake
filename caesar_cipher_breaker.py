#!/usr/bin/env python3
"""
Caesar Cipher Breaker
Breaks Caesar ciphers using frequency analysis and brute force
"""

import string
from frequency_analysis import FrequencyAnalyzer

class CaesarBreaker:
    def __init__(self):
        self.analyzer = FrequencyAnalyzer()
    
    def decrypt_with_shift(self, ciphertext, shift):
        """Decrypt Caesar cipher with given shift value"""
        result = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - ascii_offset - shift) % 26
                result += chr(shifted + ascii_offset)
            else:
                result += char
        return result
    
    def brute_force_attack(self, ciphertext):
        """Try all possible shifts and return results with chi-squared scores"""
        results = []
        
        print("Brute Force Attack Results:")
        print("=" * 60)
        print(f"{'Shift':<6} {'Chi-Squared':<12} {'Plaintext Preview':<40}")
        print("-" * 60)
        
        for shift in range(26):
            decrypted = self.decrypt_with_shift(ciphertext, shift)
            chi_squared = self.analyzer.calculate_chi_squared(decrypted)
            preview = decrypted[:40] + "..." if len(decrypted) > 40 else decrypted
            
            results.append((shift, chi_squared, decrypted))
            print(f"{shift:<6} {chi_squared:<12.2f} {preview:<40}")
        
        # Sort by chi-squared (lower is better)
        results.sort(key=lambda x: x[1])
        return results
    
    def frequency_attack(self, ciphertext):
        """Use frequency analysis to find most likely shift"""
        # Find most common letter in ciphertext
        freq_data = self.analyzer.analyze_text(ciphertext)
        most_common = max(freq_data.items(), key=lambda x: x[1]['count'])
        most_common_letter = most_common[0]
        
        # Assume most common letter maps to 'E'
        shift = (ord(most_common_letter) - ord('E')) % 26
        decrypted = self.decrypt_with_shift(ciphertext, shift)
        
        print("Frequency Analysis Attack:")
        print("=" * 40)
        print(f"Most common letter in ciphertext: {most_common_letter}")
        print(f"Assuming it maps to 'E', shift = {shift}")
        print(f"Decrypted text: {decrypted}")
        
        return shift, decrypted
    
    def break_cipher(self, ciphertext):
        """Main function to break Caesar cipher"""
        print(f"Breaking Caesar cipher for: {ciphertext[:50]}...")
        print()
        
        # Try frequency analysis first
        freq_shift, freq_result = self.frequency_attack(ciphertext)
        freq_chi = self.analyzer.calculate_chi_squared(freq_result)
        
        print(f"Chi-squared for frequency attack: {freq_chi:.2f}")
        print()
        
        # Try brute force
        brute_results = self.brute_force_attack(ciphertext)
        
        print()
        print("Best candidates:")
        print("=" * 60)
        for i, (shift, chi_squared, decrypted) in enumerate(brute_results[:3]):
            print(f"{i+1}. Shift {shift} (Chi²: {chi_squared:.2f})")
            print(f"   {decrypted}")
            print()
        
        return brute_results[0]  # Return best result

def main():
    breaker = CaesarBreaker()
    
    print("Caesar Cipher Breaker")
    print("Enter encrypted text (or 'quit' to exit):")
    
    while True:
        ciphertext = input("\n> ")
        if ciphertext.lower() == 'quit':
            break
        
        if ciphertext.strip():
            best_shift, best_chi, best_plaintext = breaker.break_cipher(ciphertext)
            print(f"Most likely solution:")
            print(f"Shift: {best_shift}")
            print(f"Plaintext: {best_plaintext}")

if __name__ == "__main__":
    main()