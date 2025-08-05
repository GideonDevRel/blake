#!/usr/bin/env python3
"""
Hash Collision Finder (Educational)
Demonstrates hash collisions using simplified hash functions for educational purposes
WARNING: This is for educational use only - understanding cryptographic weaknesses
"""

import hashlib
import random
import string
import time
from collections import defaultdict

class HashCollisionFinder:
    def __init__(self):
        self.collision_found = False
    
    def simple_hash(self, data, bits=16):
        """Simple hash function that truncates SHA-256 to specified bits"""
        full_hash = hashlib.sha256(data.encode()).hexdigest()
        # Truncate to specified number of bits (in hex characters)
        hex_chars = bits // 4
        return full_hash[:hex_chars]
    
    def birthday_attack(self, hash_func, target_bits=16, max_attempts=100000):
        """Demonstrate birthday attack to find hash collisions"""
        print(f"Birthday Attack on {target_bits}-bit hash")
        print("=" * 50)
        
        hash_table = defaultdict(list)
        attempts = 0
        start_time = time.time()
        
        while attempts < max_attempts:
            # Generate random input
            random_input = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            hash_value = hash_func(random_input, target_bits)
            
            # Check if we've seen this hash before
            if hash_value in hash_table:
                collision_inputs = hash_table[hash_value]
                for existing_input in collision_inputs:
                    if existing_input != random_input:
                        elapsed = time.time() - start_time
                        print(f"COLLISION FOUND after {attempts} attempts in {elapsed:.2f} seconds!")
                        print(f"Input 1: '{existing_input}'")
                        print(f"Input 2: '{random_input}'")
                        print(f"Hash:    {hash_value}")
                        print(f"Full hashes:")
                        print(f"  SHA-256('{existing_input}') = {hashlib.sha256(existing_input.encode()).hexdigest()}")
                        print(f"  SHA-256('{random_input}') = {hashlib.sha256(random_input.encode()).hexdigest()}")
                        return existing_input, random_input, hash_value, attempts
            
            hash_table[hash_value].append(random_input)
            attempts += 1
            
            if attempts % 1000 == 0:
                print(f"Attempts: {attempts}, Unique hashes: {len(hash_table)}")
        
        print(f"No collision found after {max_attempts} attempts")
        return None, None, None, attempts
    
    def preimage_attack_demo(self, target_hash, hash_func, target_bits=16, max_attempts=50000):
        """Demonstrate preimage attack (finding input that produces specific hash)"""
        print(f"Preimage Attack on {target_bits}-bit hash")
        print(f"Target hash: {target_hash}")
        print("=" * 50)
        
        attempts = 0
        start_time = time.time()
        
        while attempts < max_attempts:
            # Generate random input
            random_input = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            hash_value = hash_func(random_input, target_bits)
            
            if hash_value == target_hash:
                elapsed = time.time() - start_time
                print(f"PREIMAGE FOUND after {attempts} attempts in {elapsed:.2f} seconds!")
                print(f"Input: '{random_input}'")
                print(f"Hash: {hash_value}")
                return random_input, attempts
            
            attempts += 1
            
            if attempts % 5000 == 0:
                print(f"Attempts: {attempts}")
        
        print(f"No preimage found after {max_attempts} attempts")
        return None, attempts
    
    def demonstrate_weak_hash(self):
        """Demonstrate collisions in a very weak hash function"""
        print("Demonstrating Weak Hash Function")
        print("=" * 40)
        
        def weak_hash(data):
            """Extremely weak hash that only looks at first and last character"""
            if len(data) < 2:
                return "00"
            return f"{ord(data[0]):02x}{ord(data[-1]):02x}"
        
        print("Weak hash function: hash(data) = hex(first_char) + hex(last_char)")
        
        # Find collision easily
        collisions = []
        test_strings = ["ab", "ax", "bb", "bx", "hello", "hallo", "test", "tent"]
        
        hash_map = {}
        for string in test_strings:
            hash_val = weak_hash(string)
            if hash_val in hash_map:
                print(f"COLLISION: '{hash_map[hash_val]}' and '{string}' both hash to {hash_val}")
                collisions.append((hash_map[hash_val], string, hash_val))
            else:
                hash_map[hash_val] = string
        
        if not collisions:
            print("Creating deliberate collision:")
            str1 = "apple"
            str2 = "apxle"  # Same first and last character
            hash1 = weak_hash(str1)
            hash2 = weak_hash(str2)
            print(f"'{str1}' hashes to {hash1}")
            print(f"'{str2}' hashes to {hash2}")
            if hash1 == hash2:
                print("COLLISION FOUND!")
    
    def analyze_hash_distribution(self, hash_func, target_bits=8, num_samples=10000):
        """Analyze distribution of hash values"""
        print(f"Hash Distribution Analysis ({target_bits}-bit, {num_samples} samples)")
        print("=" * 60)
        
        hash_counts = defaultdict(int)
        
        for i in range(num_samples):
            random_input = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            hash_value = hash_func(random_input, target_bits)
            hash_counts[hash_value] += 1
        
        # Statistics
        expected_per_hash = num_samples / (2 ** target_bits)
        unique_hashes = len(hash_counts)
        max_count = max(hash_counts.values())
        min_count = min(hash_counts.values())
        
        print(f"Total samples: {num_samples}")
        print(f"Possible hash values: {2 ** target_bits}")
        print(f"Expected samples per hash: {expected_per_hash:.2f}")
        print(f"Unique hashes generated: {unique_hashes}")
        print(f"Max occurrences of any hash: {max_count}")
        print(f"Min occurrences of any hash: {min_count}")
        
        # Show hash collisions
        collisions = {h: count for h, count in hash_counts.items() if count > 1}
        print(f"Hash values with collisions: {len(collisions)}")
        
        if collisions:
            print("Top collisions:")
            sorted_collisions = sorted(collisions.items(), key=lambda x: x[1], reverse=True)
            for hash_val, count in sorted_collisions[:5]:
                print(f"  {hash_val}: {count} occurrences")

def main():
    finder = HashCollisionFinder()
    
    print("Hash Collision Finder (Educational)")
    print("WARNING: For educational purposes only!")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Birthday attack (find any collision)")
        print("2. Preimage attack (find input for specific hash)")
        print("3. Demonstrate weak hash function")
        print("4. Analyze hash distribution")
        print("5. Quit")
        
        choice = input("\n> ")
        
        if choice == '1':
            print("Enter number of bits for hash (8-32, default 16):")
            bits_input = input("> ")
            bits = int(bits_input) if bits_input.isdigit() else 16
            bits = max(8, min(32, bits))  # Clamp between 8 and 32
            
            finder.birthday_attack(finder.simple_hash, bits)
            
        elif choice == '2':
            print("Enter target hash (or press Enter for random):")
            target = input("> ").strip()
            if not target:
                # Generate random target
                random_input = ''.join(random.choices(string.ascii_letters, k=5))
                target = finder.simple_hash(random_input, 16)
                print(f"Generated random target: {target}")
            
            finder.preimage_attack_demo(target, finder.simple_hash, 16)
            
        elif choice == '3':
            finder.demonstrate_weak_hash()
            
        elif choice == '4':
            print("Enter number of bits for analysis (4-16, default 8):")
            bits_input = input("> ")
            bits = int(bits_input) if bits_input.isdigit() else 8
            bits = max(4, min(16, bits))  # Clamp for reasonable analysis time
            
            finder.analyze_hash_distribution(finder.simple_hash, bits)
            
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()