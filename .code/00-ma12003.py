"""Jupyter setup for MA12003"""
# Add code directory to path to pick up model solutions
import sys
import os
sys.path.insert(0,os.path.expanduser('~')+"/ma12003.git/.code/")

# Make pytest available
import pytest

def run_tests():
    """Run pytest on all tests in the current notebook"""
    pytest.main(args=["-v","--tb=short","--color=yes","--timeout=5","-W ignore::DeprecationWarning"])