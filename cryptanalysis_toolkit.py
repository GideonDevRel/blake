#!/usr/bin/env python3
"""
Cryptanalysis Toolkit
Main interface for all cryptanalysis tools
Educational tool for learning cryptographic analysis techniques
"""

import sys
import os
from frequency_analysis import FrequencyAnalyzer
from caesar_cipher_breaker import CaesarBreaker
from substitution_cipher_solver import SubstitutionSolver
from vigenere_cipher_breaker import VigenereBreaker
from hash_collision_finder import HashCollisionFinder

class CryptanalysisToolkit:
    def __init__(self):
        self.freq_analyzer = FrequencyAnalyzer()
        self.caesar_breaker = CaesarBreaker()
        self.substitution_solver = SubstitutionSolver()
        self.vigenere_breaker = VigenereBreaker()
        self.hash_finder = HashCollisionFinder()
    
    def display_banner(self):
        """Display toolkit banner"""
        print("=" * 60)
        print("         CRYPTANALYSIS TOOLKIT")
        print("         Educational Use Only")
        print("=" * 60)
        print("Available Tools:")
        print("1. Frequency Analysis")
        print("2. Caesar Cipher Breaker")
        print("3. Substitution Cipher Solver")
        print("4. Vigenère Cipher Breaker")
        print("5. Hash Collision Finder")
        print("6. Cipher Type Identifier")
        print("7. Batch Analysis")
        print("8. Help")
        print("9. Exit")
        print("=" * 60)
    
    def identify_cipher_type(self, ciphertext):
        """Attempt to identify the type of cipher used"""
        print("Cipher Type Analysis")
        print("=" * 30)
        
        # Calculate Index of Coincidence
        ic = self.vigenere_breaker.index_of_coincidence(ciphertext)
        print(f"Index of Coincidence: {ic:.4f}")
        
        # Analyze frequency distribution
        freq_data = self.freq_analyzer.analyze_text(ciphertext)
        chi_squared = self.freq_analyzer.calculate_chi_squared(ciphertext)
        print(f"Chi-squared statistic: {chi_squared:.2f}")
        
        # Check for patterns
        words = ciphertext.upper().split()
        single_char_words = [w for w in words if len(w) == 1]
        repeated_chars = len([c for c in ciphertext.upper() if c.isalpha() and ciphertext.upper().count(c) > len(ciphertext) * 0.1])
        
        print(f"Single character words: {len(single_char_words)}")
        print(f"Highly repeated characters: {repeated_chars}")
        
        # Make recommendations
        print("\nRecommendations:")
        if ic > 0.065:
            if chi_squared < 50:
                print("- Likely plaintext or very weak cipher")
            elif single_char_words > 0:
                print("- Possibly monoalphabetic substitution cipher")
                print("- Try: Substitution Cipher Solver")
            else:
                print("- Possibly Caesar cipher")
                print("- Try: Caesar Cipher Breaker")
        elif 0.045 < ic < 0.065:
            print("- Possibly Vigenère cipher with short key")
            print("- Try: Vigenère Cipher Breaker")
        elif ic < 0.045:
            print("- Likely polyalphabetic cipher or random data")
            print("- Try: Vigenère Cipher Breaker")
        else:
            print("- Uncertain cipher type")
            print("- Try multiple tools")
    
    def batch_analysis(self, ciphertext):
        """Run multiple analysis tools on the same ciphertext"""
        print("Batch Analysis Mode")
        print("=" * 40)
        print(f"Analyzing: {ciphertext[:50]}...")
        print()
        
        # 1. Frequency Analysis
        print("1. FREQUENCY ANALYSIS:")
        print("-" * 20)
        self.freq_analyzer.display_frequency_table(ciphertext)
        print()
        
        # 2. Cipher Type Identification
        print("2. CIPHER TYPE IDENTIFICATION:")
        print("-" * 30)
        self.identify_cipher_type(ciphertext)
        print()
        
        # 3. Caesar Cipher Attempt
        print("3. CAESAR CIPHER ANALYSIS:")
        print("-" * 25)
        try:
            caesar_result = self.caesar_breaker.break_cipher(ciphertext)
            print("Caesar cipher attempt completed.")
        except Exception as e:
            print(f"Caesar analysis failed: {e}")
        print()
        
        # 4. Quick Vigenère test
        print("4. VIGENÈRE CIPHER ANALYSIS:")
        print("-" * 27)
        try:
            ic = self.vigenere_breaker.index_of_coincidence(ciphertext)
            if ic < 0.065:  # Likely polyalphabetic
                print("Running Vigenère analysis...")
                vigenere_result = self.vigenere_breaker.break_vigenere(ciphertext)
            else:
                print("IC suggests monoalphabetic cipher - skipping Vigenère analysis")
        except Exception as e:
            print(f"Vigenère analysis failed: {e}")
        print()
    
    def display_help(self):
        """Display help information"""
        help_text = """
CRYPTANALYSIS TOOLKIT HELP
===========================

This toolkit provides educational implementations of classic cryptanalysis techniques:

1. FREQUENCY ANALYSIS
   - Analyzes letter frequency distribution
   - Calculates chi-squared statistics
   - Useful for all substitution ciphers

2. CAESAR CIPHER BREAKER
   - Brute force attack (tries all 26 shifts)
   - Frequency-based attack
   - Best for simple Caesar ciphers

3. SUBSTITUTION CIPHER SOLVER
   - Pattern matching analysis
   - Frequency-based letter mapping
   - Interactive key adjustment
   - Best for monoalphabetic substitution

4. VIGENÈRE CIPHER BREAKER
   - Kasiski examination
   - Index of Coincidence calculation
   - Key length determination
   - Best for polyalphabetic ciphers

5. HASH COLLISION FINDER
   - Birthday attack demonstration
   - Preimage attack simulation
   - Hash distribution analysis
   - Educational hash security tool

6. CIPHER TYPE IDENTIFIER
   - Statistical analysis
   - Pattern recognition
   - Provides tool recommendations

7. BATCH ANALYSIS
   - Runs multiple tools automatically
   - Comprehensive cipher analysis
   - Good starting point for unknown ciphers

TIPS:
- Start with Cipher Type Identifier for unknown ciphers
- Use Batch Analysis for comprehensive analysis
- All tools are designed for educational purposes
- Results may not be perfect for complex ciphers

WARNING: These tools are for educational use only!
Do not use for breaking real-world encryption.
        """
        print(help_text)
    
    def run(self):
        """Main toolkit interface"""
        self.display_banner()
        
        while True:
            try:
                choice = input("\nSelect tool (1-9): ").strip()
                
                if choice == '1':
                    print("\n" + "="*50)
                    print("FREQUENCY ANALYSIS")
                    print("="*50)
                    text = input("Enter text to analyze: ")
                    if text:
                        self.freq_analyzer.display_frequency_table(text)
                        chi_squared = self.freq_analyzer.calculate_chi_squared(text)
                        print(f"\nChi-squared: {chi_squared:.2f}")
                
                elif choice == '2':
                    print("\n" + "="*50)
                    print("CAESAR CIPHER BREAKER")
                    print("="*50)
                    ciphertext = input("Enter Caesar cipher text: ")
                    if ciphertext:
                        self.caesar_breaker.break_cipher(ciphertext)
                
                elif choice == '3':
                    print("\n" + "="*50)
                    print("SUBSTITUTION CIPHER SOLVER")
                    print("="*50)
                    ciphertext = input("Enter substitution cipher text: ")
                    if ciphertext:
                        self.substitution_solver.solve_cipher(ciphertext)
                
                elif choice == '4':
                    print("\n" + "="*50)
                    print("VIGENÈRE CIPHER BREAKER")
                    print("="*50)
                    ciphertext = input("Enter Vigenère cipher text: ")
                    if ciphertext:
                        self.vigenere_breaker.break_vigenere(ciphertext)
                
                elif choice == '5':
                    print("\n" + "="*50)
                    print("HASH COLLISION FINDER")
                    print("="*50)
                    print("Launching hash collision tool...")
                    from hash_collision_finder import main as hash_main
                    hash_main()
                
                elif choice == '6':
                    print("\n" + "="*50)
                    print("CIPHER TYPE IDENTIFIER")
                    print("="*50)
                    ciphertext = input("Enter cipher text to identify: ")
                    if ciphertext:
                        self.identify_cipher_type(ciphertext)
                
                elif choice == '7':
                    print("\n" + "="*50)
                    print("BATCH ANALYSIS")
                    print("="*50)
                    ciphertext = input("Enter cipher text for batch analysis: ")
                    if ciphertext:
                        self.batch_analysis(ciphertext)
                
                elif choice == '8':
                    self.display_help()
                
                elif choice == '9':
                    print("Goodbye!")
                    break
                
                else:
                    print("Invalid choice. Please enter 1-9.")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("Please try again.")

def main():
    toolkit = CryptanalysisToolkit()
    toolkit.run()

if __name__ == "__main__":
    main()