# test_quantumglide.py
"""
Tests for QuantumGlide module.
"""

import unittest
from quantumglide import QuantumGlide

class TestQuantumGlide(unittest.TestCase):
    """Test cases for QuantumGlide class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumGlide()
        self.assertIsInstance(instance, QuantumGlide)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumGlide()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
