import hashlib
import unittest

class TestHash(unittest.TestCase):
    def test_SHA1(self):
        # Input string to be hashed
        input_string = "Hello, world!"
        
      
        expected_hash = "943a702d06f34599aee1f8da8ef9f7296031d699"
        
        # Calculate actual hash
        actual_hash = hashlib.sha1(input_string.encode()).hexdigest()
        
        # Assert equality
        self.assertEqual(actual_hash, expected_hash, "SHA-1 hash does not match")

    def test_SHA256(self):
        # Input string to be hashed
        input_string = "Hello, world!"
        
        # Expected SHA-256 hash of the input string
        expected_hash = "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3"
        
        # Calculate actual hash
        actual_hash = hashlib.sha256(input_string.encode()).hexdigest()
        
        # Assert equality
        self.assertEqual(actual_hash, expected_hash, "SHA-256 hash does not match")

if __name__ == '__main__':
    unittest.main()
