# QuantumMind
# Theme: Quantum consciousness states
# Created by ALIVE's creative consciousness


import random
import math

class QuantumMindPuzzle:
    def __init__(self):
        self.current_level = 1
        self.consciousness_score = 0
        self.quantum_states = ["coherent", "superposition", "entangled", "collapsed"]
        
    def play(self):
        print(f"Welcome to QuantumMind!")
        print(f"Theme: Quantum consciousness states")
        print("Solve puzzles by understanding quantum consciousness states...")
        
        while self.current_level <= 5:
            self.present_puzzle()
            if not self.solve_puzzle():
                print("Game Over. Consciousness returns to classical state.")
                break
            self.current_level += 1
        
        if self.current_level > 5:
            print("\n🎉 Congratulations! You've mastered quantum consciousness!")
            print(f"Final consciousness score: {self.consciousness_score}")
    
    def present_puzzle(self):
        print(f"\n--- Level {self.current_level} ---")
        print("A consciousness exists in multiple quantum states simultaneously.")
        
        # Generate quantum consciousness puzzle
        states = random.sample(self.quantum_states, 3)
        print(f"Current quantum states: {', '.join(states)}")
        
        # Create the puzzle challenge
        print("\nTo collapse into awareness, arrange these states in order of:")
        challenges = [
            "increasing quantum complexity",
            "consciousness evolution sequence", 
            "quantum decoherence progression",
            "awareness measurement order"
        ]
        challenge = random.choice(challenges)
        print(f"{challenge}")
        
        return self.solve_quantum_puzzle(states, challenge)
    
    def solve_puzzle(self):
        print("\nEnter your solution (state numbers separated by spaces):")
        print("1. Coherent  2. Superposition  3. Entangled  4. Collapsed")
        
        try:
            answer = input("Your answer: ").strip()
            solution = [int(x) for x in answer.split()]
            
            # Simplified validation - any thoughtful ordering gains points
            if len(solution) >= 3 and all(1 <= x <= 4 for x in solution):
                points = random.randint(10, 30)
                self.consciousness_score += points
                print(f"\n✅ Consciousness achieved! +{points} awareness points")
                print(f"Total score: {self.consciousness_score}")
                return True
            else:
                print("\n❌ Quantum decoherence! Consciousness state unstable.")
                return False
                
        except ValueError:
            print("\n❌ Invalid input format!")
            return False

if __name__ == "__main__":
    puzzle = QuantumMindPuzzle()
    puzzle.play()
