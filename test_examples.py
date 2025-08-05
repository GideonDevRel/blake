#!/usr/bin/env python3
"""
Test Examples for Cryptanalysis Toolkit
Run this to test all tools with sample data
"""

from frequency_analysis import FrequencyAnalyzer
from caesar_cipher_breaker import CaesarBreaker
from substitution_cipher_solver import SubstitutionSolver
from vigenere_cipher_breaker import VigenereBreaker
from hash_collision_finder import HashCollisionFinder

def test_frequency_analysis():
    print("="*50)
    print("TESTING FREQUENCY ANALYSIS")
    print("="*50)
    
    analyzer = FrequencyAnalyzer()
    test_text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    
    print(f"Text: {test_text}")
    analyzer.display_frequency_table(test_text)
    chi_squared = analyzer.calculate_chi_squared(test_text)
    print(f"Chi-squared: {chi_squared:.2f}")
    print()

def test_caesar_cipher():
    print("="*50)
    print("TESTING CAESAR CIPHER BREAKER")
    print("="*50)
    
    breaker = CaesarBreaker()
    
    # Test cases
    test_cases = [
        ("KHOOR ZRUOG", "Caesar cipher with shift 3"),
        ("WKH TXLFN EURZQ IRA", "Another Caesar cipher"),
    ]
    
    for ciphertext, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Ciphertext: {ciphertext}")
        
        # Quick brute force
        results = breaker.brute_force_attack(ciphertext)
        best_shift, best_chi, best_plaintext = results[0]
        print(f"Best result - Shift {best_shift}: {best_plaintext}")
        print()

def test_substitution_cipher():
    print("="*50)
    print("TESTING SUBSTITUTION CIPHER SOLVER")
    print("="*50)
    
    solver = SubstitutionSolver()
    
    # Simple substitution (A->Z, B->Y, etc.)
    ciphertext = "GSV JFRXP YILDM ULC QFNKH LEVI GSV OZAB WLT"
    print(f"Ciphertext: {ciphertext}")
    
    # Just do frequency analysis part
    freq_key = solver.frequency_based_attack(ciphertext)
    result = solver.apply_substitution(ciphertext, freq_key)
    
    print("Frequency-based mapping attempt:")
    print(f"Result: {result}")
    print()

def test_vigenere_cipher():
    print("="*50)
    print("TESTING VIGENÈRE CIPHER BREAKER")
    print("="*50)
    
    breaker = VigenereBreaker()
    
    # Test with known Vigenère cipher
    ciphertext = "LXFOPVEFRNHR DXKRQREFMTZX"  # "ATTACKATDAWN" with key "LEMON"
    print(f"Ciphertext: {ciphertext}")
    
    ic = breaker.index_of_coincidence(ciphertext)
    print(f"Index of Coincidence: {ic:.4f}")
    
    if ic < 0.065:
        print("IC suggests polyalphabetic cipher - good for Vigenère test")
    
    # Find repeated sequences
    repeated = breaker.find_repeated_sequences(ciphertext)
    print(f"Repeated sequences found: {len(repeated)}")
    print()

def test_hash_collisions():
    print("="*50)
    print("TESTING HASH COLLISION FINDER")
    print("="*50)
    
    finder = HashCollisionFinder()
    
    # Test simple hash function
    test_inputs = ["hello", "world", "test", "collision"]
    print("Testing simple hash function (16-bit):")
    for inp in test_inputs:
        hash_val = finder.simple_hash(inp, 16)
        print(f"  hash('{inp}') = {hash_val}")
    
    print("\nTesting weak hash function:")
    finder.demonstrate_weak_hash()
    print()

def run_all_tests():
    print("CRYPTANALYSIS TOOLKIT - AUTOMATED TESTS")
    print("="*60)
    
    test_frequency_analysis()
    test_caesar_cipher()
    test_substitution_cipher()
    test_vigenere_cipher()
    test_hash_collisions()
    
    print("="*60)
    print("ALL TESTS COMPLETED!")
    print("="*60)

if __name__ == "__main__":
    run_all_tests()