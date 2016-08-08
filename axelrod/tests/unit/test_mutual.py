"""Tests for strategies Desperate, Hopeless, Willing, and Grim"""
import axelrod

from .test_player import TestPlayer

C, D = axelrod.Actions.C, axelrod.Actions.D

class TestDesperate(TestPlayer):

    name = "Desperate"
    player = axelrod.Desperate
    expected_classifier = {
        'memory_depth': 1,  
        'stochastic': False,
        'makes_use_of': set(),
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        """
        Test that initial strategy defects.
        """
        self.first_play_test(D)

    def test_responses(self):

        self.responses_test([C]* 4, [D] * 4, [D])
        self.responses_test([D, D, C], [C, C, D], [D])
<<<<<<< HEAD
        self.responses_test([D, D, D], [C, C, D], [C])
=======
>>>>>>> e4e4fd4b1c41db1ad9cd3ca50c2396ee94e88e50

class TestHopeless(TestPlayer):

    name = "Hopeless"
    player = axelrod.Hopeless
    expected_classifier = {
        'memory_depth': 1,  
        'stochastic': False,
        'makes_use_of': set(),
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        """
        Test that initial strategy cooperates.
        """
        self.first_play_test(C)

    def test_responses(self):

        self.responses_test([C] * 4, [D] * 4, [C])
        self.responses_test([D] * 5, [C] * 5, [C])
        self.responses_test([C, D, C], [C, C, C], [D])

class TestWilling(TestPlayer):

    name = "Willing"
    player = axelrod.Willing
    expected_classifier = {
        'memory_depth': 1,  
        'stochastic': False,
        'makes_use_of': set(),
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        """
        Test that initial strategy cooperates.
        """
        self.first_play_test(C)

    def test_responses(self):

        self.responses_test([C] * 4, [D] * 4, [C])
        self.responses_test([D] * 5, [C] * 5, [C])
        self.responses_test([C, C, D], [C, C, D], [D])

class TestGrim(TestPlayer):

    name = "Grim"
    player = axelrod.Grim
    expected_classifier = {
        'memory_depth': 1,  # Long memory
        'stochastic': False,
        'makes_use_of': set(),
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        """
        Test that initial strategy defects.
        """
        self.first_play_test(D)

    def test_responses(self):

        self.responses_test([D] * 4, [D] * 4, [D])
        self.responses_test([D] * 5, [C] * 5, [D])
        self.responses_test([D, D, C], [C, D, C], [C])

