import unittest
import hashlib

class TestHash(unittest.TestCase):
    def test_SHA1(self):
        input_string = "HI"
        
        # Expected SHA-1 hash of the input string
        expected_hash = "253420c1158bc6382093d409ce2e9cff5806e980"
        
        actual_hash = hashlib.sha1(input_string.encode()).hexdigest()
        
        # Check if the actual hash matches the expected hash
        self.assertEqual(actual_hash, expected_hash, "SHA-1 hash does not match")

if __name__ == '__main__':
    unittest.main()
